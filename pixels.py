from PIL import Image

#Accepts image filename as argument and returns
#number of pixels.
def pixel_count(image):
    img = Image.open(image)
    pixels = img.height * img.width
    return pixels
