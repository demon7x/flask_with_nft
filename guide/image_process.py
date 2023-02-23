import random
import numpy as np
from PIL import Image
import colorsys
from math import *

def change_hue(rgb):
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h = h + 0.001
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return r, g, b

def chage_color(rgb):
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h = h + 0.001
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return r, g, b

im = Image.new("RGB", (1762,1173))
im = np.array(im)
print(im.shape)

#re = random.randint(0, 255)
#gr = random.randint(0, 255)
#bl = random.randint(0, 255)
for r in range(0,1173):
    re = random.randint(0, 255)
    gr = random.randint(0, 255)
    bl = random.randint(0, 255)
    im[r][0]=[re,gr,bl]
    for c in range(1,1762):
        cr,cg,cb = change_hue(im[r][c-1])
        im[r][c]=[cr,cg,cb]
img = Image.fromarray(im, 'RGB')

img.show()