This is the blueprint for duplication and simplification of the projects creation for reels and youtube videos


1. It goes through all the json files inside of "json" folder
2. Loops through all the array items and creates new projects based on the information in json object.
    1. It gets blueprint project copied to the "theme" named folder inside of NEW_PROJECTS folder.
    2. It copies the image and calls it mainImage.jpg or creates a new one
    3. Creates txt file for the voiceover creation inside the txt folder
    4. Creates empty voiceover.mp3 file
    5. Copies the theme related intro and outro to videos folder
3. Runs the jsx script from inside the folder to adjust the projects data, like texts, image and videos.


Have fun!




TODO's
1. Enrich the model with welcoming voiceover
2. Enrich the model with closing voiceover
3. Make automatic creation with API of the voiceovers
4. Make automatic creation of 5 images based on the voiceover so later on i can choose which one to modify


TODO's video editing team
1. Create template for general use
2. Create intro and outro for the themes
3. Create the identicator to use for all the hidden parts