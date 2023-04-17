import sys
import os
from PIL import Image

original_folder = sys.argv[1]
new_folder = sys.argv[2]

#original_folder = 'pokedex'
#new_folder = 'nuevo'
max_size = 400

new_folder_path = f'./{new_folder}'

if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)
    print('new folder created')
else:
    print('perfecto, la carpeta new ya existe')

for filename in os.listdir(original_folder):
   if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
       img = Image.open(os.path.join(original_folder, filename))
       img.thumbnail((max_size, max_size))
       img.save(os.path.join(new_folder_path, os.path.splitext(filename)[0] + '.png'), 'PNG')
       #ith Image.open(os.path.join(original_folder, filename)) as img:
            #rgb_img = img.convert('RGB')
           #png_image = rgb_img.convert('PNG')
           #png_image.save(os.path.join(new_folder_path, os.path.splitext(filename)[0] + '.png'), 'PNG')
   else:
        continue


