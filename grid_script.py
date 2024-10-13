from PIL import Image
import os

# Path to the folder containing images
image_folder = './folder/'  # Folder containing the images

# Size of each individual image
image_width, image_height = 150, 150  # Adjust according to the size of your images

# Number of images per row and column
images_per_row = 5  # Adjust according to how many images you want per row
images_per_column = 5  # Adjust according to how many images you want per column

# Create a new empty image with the necessary size
grid_width = images_per_row * image_width
grid_height = images_per_column * image_height
grid_image = Image.new('RGB', (grid_width, grid_height), color=(255, 255, 255))  # White background

# Load images and paste them into the grid
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('gif', 'png', 'jpg', 'jpeg'))]

for index, image_file in enumerate(image_files):
    if index >= images_per_row * images_per_column:
        break  # Limit the number of images to fit within the grid

    img = Image.open(os.path.join(image_folder, image_file))

    if img.format == 'GIF':
        img = img.convert('RGBA')  # Convert GIF to RGBA
        img = img.resize((image_width, image_height))  # Resize the image
        img = img.convert('RGB')  # Convert to RGB for saving as JPG
    else:
        img = img.resize((image_width, image_height))  # Resize the image

    # Calculate the x and y positions
    x = (index % images_per_row) * image_width
    y = (index // images_per_row) * image_height

    # Paste the image into the grid
    grid_image.paste(img, (x, y))

# Save the final image as JPEG or PNG
grid_image.save('output_grid_image.jpg')  # Or 'output_grid_image.png' for PNG
