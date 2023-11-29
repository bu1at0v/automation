// Create a new project
app.newProject();

var project = app.project;

// Function to read JSON File
function readJSONFile(filePath) {
    var file = new File(filePath);
    if (file.exists) {
        file.open('r');
        var data = file.read();
        file.close();
        return JSON.parse(data);
    } else {
        alert("File not found.");
        return null;
    }
}

// Path to JSON file
var jsonFilePath = "json/videos.json";
var jsonData = readJSONFile(jsonFilePath);

console.log(jsonData);

if (jsonData) {
    // Assuming jsonData contains necessary data for text replacement

    // Import Intro
    var introFile = new File("path/to/your/intro/file");
    var importOptions = new ImportOptions(introFile);
    var introItem = project.importFile(importOptions);

    // Create a new composition
    var compSettings = [1920, 1080, 1, 30, 30]; // Width, Height, Pixel Aspect Ratio, Frame Rate, Duration in seconds
    var comp = project.items.addComp('MainComp', compSettings[0], compSettings[1], compSettings[2], compSettings[3], compSettings[4]);

    // Add intro to the composition
    comp.layers.add(introItem);

    // Add text layer with animation
    var textLayer = comp.layers.addText(jsonData.text); // Replace 'jsonData.text' with the appropriate field from your JSON

    // Apply your text animation presets or keyframes here

    // Import Outro
    var outroFile = new File("path/to/your/outro/file");
    importOptions = new ImportOptions(outroFile);
    var outroItem = project.importFile(importOptions);

    // Add outro to the composition
    comp.layers.add(outroItem);
}
