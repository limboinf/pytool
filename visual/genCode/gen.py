# coding=utf-8
__author__ = 'fang'
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 背景颜色随机:
def rndBgColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 字体颜色随机:
def rndFontColor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 生成二维码
def genTDCode():
    width = 60 *4
    height = 60
    img = Image.new('RGB', (width, height), 0xffffff)
    font = ImageFont.truetype('Libian.ttc', 50)         # 创建Font对象
    draw = ImageDraw.Draw(img)                          # 创建Draw对象
    # 填充每一个像素
    for w in range(width):
        for h in range(height):
            draw.point((w, h), fill=rndBgColor())

    # 打印文字
    for t in range(5):
        draw.text(
            (50 * t + 10, 0),
            rndChar(),
            font=font,
            fill=rndFontColor()
            # fill=0x000000     # 纯黑
        )
    # 模糊
    img = img.filter(ImageFilter.BLUR)
    img.save('code.jpg', 'jpeg')
    img.show()

if __name__ == '__main__':
    genTDCode()