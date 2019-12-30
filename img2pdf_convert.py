# importing necessary libraries 
import img2pdf 
from PIL import Image 
import os 
import argparse


def parseArg():
    """
    Parse arguements to the detect module.
    """
    parser = argparse.ArgumentParser(description='Converting image file to pdf')
    parser.add_argument("--img", dest="img", help="File path of image file", default='./test.png', type = str)
    parser.add_argument('--dest', dest='dest', help='Destination file path', default='./test.pdf', type=str)

    return parser.parse_args()


args = parseArg() # parse the command line arguments

# file paths
img_path = args.img
pdf_path = args.dest


# opening image 
image = Image.open(img_path) 

# converting into chunks using img2pdf 
pdf_bytes = img2pdf.convert(image.filename) 

# opening or creating pdf file 
file = open(pdf_path, "wb") 

# writing pdf files with chunks 
file.write(pdf_bytes) 

# closing image file 
image.close() 

# closing pdf file 
file.close() 

# output 
print("Successfully made pdf file")
