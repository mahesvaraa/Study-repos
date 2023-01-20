import os

from PIL import Image
from PIL.ImageFilter import Color3DLUT

cnt = 0
def transform(r, g, b):
    r, b, g = sorted((r, g, b))
    avg_v = r * 1 + g * 1 + b * 0.2
    r += (r - avg_v) * r
    g += (g - avg_v) * g
    b += (b - avg_v) * b
    return r, g, b

lut = Color3DLUT.generate(17, transform)

#for dirName, subDirs, fileNames in os.walk(r'E:\Новая папка\Новая папка (2)\Resources'):
for dirName, subDirs, fileNames in os.walk(r'E:\Новая папка\Новая папка (2)\Resources'):
    for file in fileNames:
        if file.endswith(('.png', '.jpg')):
            try:
                image = Image.open(os.path.join(dirName, file))#.convert('RGB')
                image.filter(lut).save(os.path.join(dirName, file))
            except:
                image = Image.open(os.path.join(dirName, file)).convert('RGB')
                image.filter(lut).save(os.path.join(dirName, file))
print(cnt)