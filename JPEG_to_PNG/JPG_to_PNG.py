from PIL import Image, ImageFilter
import sys
import os

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

for file in os.listdir(image_folder):
    img = Image.open(f'{image_folder}' + '/' + f'{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}' + '/' + f'{clean_name}.png', 'png')
    print(f"{file} done")