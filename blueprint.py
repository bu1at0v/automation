import os
import shutil
import json
import subprocess
import logging
from PIL import Image
from gtts import gTTS

# Set up logging
logging.basicConfig(filename='script.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Paths
blueprint_path = './blueprint'
new_projects_path = './NEW_PROJECTS'
json_folder_path = './ADDITIONAL/json'
base_videos_path = './ADDITIONAL/videos/shorts/themes'
img_path = './ADDITIONAL/img'
after_effects_script = './ADDITIONAL/ae_script/script.jsx'
after_effects_exe_path = "path/to/AfterFX.exe"  # Update this path

# Clear the existing log file
with open('script.log', 'w'):
    pass

try:
    # Check and clear the NEW_PROJECTS folder
    if os.path.exists(new_projects_path):
        shutil.rmtree(new_projects_path)
    os.makedirs(new_projects_path)
    logging.info(f'Prepared folder: {new_projects_path}')

    # Iterate over each JSON file in the json folder
    for json_file in os.listdir(json_folder_path):
        if json_file.endswith('.json'):
            json_path = os.path.join(json_folder_path, json_file)

            # Read JSON file
            with open(json_path, 'r') as file:
                video_data = json.load(file)  # Assuming the file contains a JSON array

                for video in video_data:
                    title = video.get("title")
                    theme = video.get('theme')
                    voiceover = video.get('voiceover')
                    if not theme or not title or not voiceover:
                        logging.warning(f'Missing theme, title, or voiceover for video in {json_file}')
                        continue

                    new_project_path = f'{new_projects_path}/{theme}/{title}'
                    shutil.copytree(blueprint_path, new_project_path)
                    logging.info(f'Created new project folder: {new_project_path}')

                    # Construct source and target paths for videos
                    source_path = os.path.join(base_videos_path, theme)
                    target_path = os.path.join(new_project_path, 'videos')

                    if os.path.exists(source_path):
                        os.makedirs(target_path, exist_ok=True)
                        # Copy files from source to target
                        for filename in os.listdir(source_path):
                            full_file_name = os.path.join(source_path, filename)
                            if os.path.isfile(full_file_name):
                                shutil.copy(full_file_name, target_path)
                                logging.info(f'Copied {filename} to {target_path}')
                    else:
                        logging.error(f'Source path does not exist: {source_path}')

                    # Image handling
                    imageUrl = video.get("imageUrl")
                    image_png = os.path.join(img_path, f'{imageUrl}.png')
                    image_jpg = os.path.join(img_path, f'{imageUrl}.jpg')
                    image_to_copy = None

                    if os.path.exists(image_png):
                        image_to_copy = image_png
                    elif os.path.exists(image_jpg):
                        image_to_copy = image_jpg

                    img_target_path = os.path.join(new_project_path, 'img')
                    os.makedirs(img_target_path, exist_ok=True)
                    new_image_path = os.path.join(img_target_path, 'mainImage.jpg')
                    new_image_diff_shown_path = os.path.join(img_target_path, 'mainImageShown.jpg')

                    if image_to_copy:    
                        shutil.copyfile(image_to_copy, new_image_path)
                        logging.info(f'Copied {image_to_copy} to {new_image_path}')
                    else:
                        # Create a placeholder image
                        placeholder_image = Image.new('RGB', (1080, 1920), color = (255, 255, 255))
                        placeholder_image.save(new_image_path)
                        logging.info(f'Created placeholder image at {new_image_path}')

                        placeholder_image = Image.new('RGB', (1080, 1920), color = (255, 255, 255))
                        placeholder_image.save(new_image_diff_shown_path)
                        logging.info(f'Created placeholder image at {new_image_diff_shown_path}')


                    # Create voiceover folder and generate MP3 file
                    voiceover_folder_path = os.path.join(new_project_path, 'voiceover')
                    os.makedirs(voiceover_folder_path, exist_ok=True)
                    mp3_file_path = os.path.join(voiceover_folder_path, 'voiceover.mp3')

                    tts = gTTS(text=voiceover, lang='en')  # Set the language as needed
                    tts.save(mp3_file_path)
                    logging.info(f'Created voiceover MP3 file: {mp3_file_path}')

                    # Create text file for voiceover
                    txt_folder_path = os.path.join(new_project_path, 'txt')
                    os.makedirs(txt_folder_path, exist_ok=True)
                    txt_filename = title.replace(' ', '') + '.txt'
                    txt_file_path = os.path.join(txt_folder_path, txt_filename)

                    with open(txt_file_path, 'w') as txt_file:
                        txt_file.write(voiceover)
                        logging.info(f'Created voiceover text file: {txt_file_path}')

                    # Uncomment the next line to run the After Effects script
                    # subprocess.call([after_effects_exe_path, "-r", after_effects_script])
                    logging.info(f'Ran After Effects script for {new_project_path}')

except Exception as e:
    logging.error(f'Error occurred: {e}')
