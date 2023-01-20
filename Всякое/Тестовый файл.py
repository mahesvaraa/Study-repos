# import os
# from PIL import Image
# from PIL.ImageFilter import Color3DLUT
#
# def transform(r, g, b):
#     r, g, b = (max(r, g, b), g, min(r, g, b))
#     avg_v = r * 0.1 + g * 0.7 + b * 0.1
#     r -= (r - avg_v) * 2
#     g -= (g - avg_v) * 0.5
#     b += (b - avg_v) * 0.5
#     return r, g, b
#
# lut = Color3DLUT.generate(17, transform)
# for (dirName, subDirs, fileNames) in os.walk(r'E:\Новая папка\Новая папка\Joystick'):
#     for file in fileNames:
#         image = Image.open(os.path.join(dirName, file)).convert('RGB')
#         image.filter(lut).save(os.path.join(r'E:\Новая папка\Новая папка\Joystick — копия', file))


import os

from PIL import Image
from PIL.ImageFilter import Color3DLUT


def transform(r, g, b):
    # if (r, g, b) == (253, 184, 50):
    #     print(file)
    r, g, b = (max(r, g, b), g, min(r, g, b))
    avg_v = r * 0.2126 + g * 0.7152 + b * 0.0722
    #r += (r - avg_v) * 0
    g += (g - avg_v) * 0.6
    #b += (b - avg_v) * 0.6
    return r, g, b

lut = Color3DLUT.generate(17, transform)
for (dirName, subDirs, fileNames) in os.walk(r'E:\Новая папка\Новая папка (2)\Resources2'):
    for file in fileNames:
        if file.endswith(('.png', '.jpg')):
            try:
                image = Image.open(os.path.join(dirName, file))#.convert('RGB')
                pixels = image.load()
            except:
                image = Image.open(os.path.join(dirName, file)).convert('RGB')
                pixels = image.load()
            print(pixels[0, 0])
