
PDF to EPS Converter
This is a simple Python script that converts all PDF files in the current directory to EPS format using the pdf2image and Pillow modules.

Requirements
Python 3.x
pdf2image module (pip install pdf2image)
Pillow module (pip install Pillow)
Poppler tools (for PDF to image conversion)
Installation
Clone or download this repository to your local machine.

Install the required modules using pip:

pip install pdf2image Pillow
Download the Poppler tools from the following link: https://poppler.freedesktop.org/

Extract the contents of the downloaded file to a directory of your choice (e.g. C:\poppler\bin)

Add the Poppler tools directory to your system path:

On Windows:
Open the Start menu and search for "Environment Variables".
Click on "Edit the system environment variables".
Click on the "Environment Variables" button.
In the "System Variables" section, find the "Path" variable and click on the "Edit" button.
Click on the "New" button and enter the path to the Poppler tools directory (e.g. C:\poppler\bin).
Click "OK" to close all windows.
Usage
Open a command prompt or terminal window in the directory containing the PDF files you want to convert.

Run the following command to convert the PDF files to EPS format:

python pdf_to_eps.py
The script will convert all PDF files in the current directory to EPS format and save them in the same directory.

Note that the script will delete the intermediate PNG files after the EPS files have been generated.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments
The pdf2image and Pillow modules were developed by Edgewood Solutions LLC and Fredrik Lundh, respectively.
The Poppler tools were developed by the Xpdf project team and the Poppler developers.
