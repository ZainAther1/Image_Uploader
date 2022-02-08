

# Importing Image and ImageFont, ImageDraw module from PIL package
from PIL import Image, ImageFont, ImageDraw



# creating a image object
image = Image.open(r'C:\Users\dell\Downloads\1.jpg')

draw = ImageDraw.Draw(image)

# specified font size
font = ImageFont.truetype(r'C:\Users\dell\Downloads\Sometime.ttf', 70)

text = 'LAUGHING IS THE \n BEST MEDICINE'

# drawing text size
draw.text((10, 10), text, fill="red", font=font, align="right")

image.show()
