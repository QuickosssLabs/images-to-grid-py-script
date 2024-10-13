Install Dependencies
Ensure you have Python installed. You also need to install the Pillow library to work with images.

To install Pillow, open a terminal and run:
"pip install Pillow"

Make sure your folder structure looks like this:
/project/
│
├── create_image_grid.py    # Your Python script
├── /folder/              # Folder containing the images
    ├── image1.gif
    ├── image2.jpg
    └── ... (other images)

The script (create_image_grid.py) and the images folder (which contains all the images you want to include in the grid) should be in the same directory.

Adjust Parameters (Optional) :
If needed, open the script and adjust the following parameters to fit your requirements:
"image_width, image_height:" Controls the size of each individual image in the grid.
"images_per_row, images_per_column:" Specifies how many images should be placed per row and per column in the grid.

These can be adjusted to control the dimensions of the final image grid.

Run the Script
Open a terminal or command prompt in the /project/ directory and run the script using Python:
"python create_image_grid.py"

The script will load images from the images folder, resize them, and assemble them into a grid.

Output :
After running the script, the final image grid will be saved as output_grid_image.jpg in the same folder as the script.
If you prefer a different format, like PNG, you can change the save format in the script:

"grid_image.save('output_grid_image.png')"