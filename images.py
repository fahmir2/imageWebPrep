from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
#filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')
filtered_img.save('blur.png', 'png')
print(img.size, img.format)