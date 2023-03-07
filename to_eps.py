import os
from pdf2image import convert_from_path
from PIL import Image

# Get the current directory
current_dir = os.getcwd()

# Set the path to the Poppler tools directory
poppler_path = os.path.join(current_dir, 'poppler-0.68.0_x86', 'poppler-0.68.0', 'bin')

# Add the Poppler tools directory to the system path
os.environ['PATH'] += os.pathsep + poppler_path

# Loop through all files in the current directory
for filename in os.listdir(current_dir):
    if filename.endswith('.pdf'):
        # Construct the input and output filenames
        input_file = os.path.join(current_dir, filename)
        output_prefix = os.path.splitext(input_file)[0]

        # Use pdf2image to convert the file to images
        pages = convert_from_path(input_file)

        # Save each page as a separate image
        for i, page in enumerate(pages):
            output_file = f"{output_prefix}_page{i+1}.png"
            page.save(output_file, 'PNG')

            # Open the PNG image and save it as EPS
            with Image.open(output_file) as img:
                eps_file = f"{output_prefix}_page{i+1}.eps"
                img.save(eps_file, 'EPS')

            # Delete the PNG file
            os.remove(output_file)
