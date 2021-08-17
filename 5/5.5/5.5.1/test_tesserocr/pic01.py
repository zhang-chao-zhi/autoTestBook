# -*- coding: utf-8 -*-
import tesserocr

from PIL import Image

image=Image.open('./yzm02.png')
image=image.convert("L") # 将图片转为灰度图
threshold=100 # 阈值设定为100
table=[]
# 进行二值化
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')
image.show()

print(tesserocr.image_to_text(image))

