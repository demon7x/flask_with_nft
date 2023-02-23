from PIL import Image
import numpy as np
import colorsys



def change_hue(rgb):
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return h
im = Image.open("../static/assets/qs/qs002.jpg")
#get image pixel rgb
im = im.convert('RGB')  # convert to RGB
width, height = im.size # get image size
pixel_values = list(im.getdata()) # get pixel values
pixel_values = np.array(pixel_values).reshape((width, height, 3)) # reshape to 2D array
print(pixel_values.shape)
for x in pixel_values[0]:
    h, s, v = colorsys.rgb_to_hsv(x[0], x[1], x[2])
    print(h,s,v)
for x in pixel_values[0]:
    print(x)