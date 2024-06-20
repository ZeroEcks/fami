import os
from wand.image import Image

MAX_WIDTH = 1080
MAX_HEIGHT = 1350

def run_instagram(output_dir='instagram'):
    # Get the current directory
    current_dir = os.getcwd()

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over all files in the current directory
    for filename in os.listdir(current_dir):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            # Open the image file
            with Image(filename=os.path.join(current_dir, filename)) as img:
                # Calculate the new height while maintaining the aspect ratio
                new_height = int((MAX_WIDTH * 2 / img.width) * img.height)
                # Resize the image
                img.resize(MAX_WIDTH * 2, new_height)
                img.extent(MAX_WIDTH * 2, MAX_HEIGHT * 2, gravity='center')
                # Save the resized image to the output directory
                img.save(filename=os.path.join(output_dir, filename))
