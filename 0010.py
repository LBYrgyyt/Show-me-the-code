#生成验证码图片

import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def get_picture():
    width = int(input("请输入宽度："))
    height = int(input("请输入高度："))
    Font = ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf",36)  
    im = Image.new('RGB',(width*4,height))
    draw = ImageDraw.Draw(im)
    for x in range(width*4):
        for y in range(height):
            draw.point((x,y),fill=(random.randint(101,255),
                                   random.randint(101,255),
                                   random.randint(101,255)))

    for i in range(4):
        draw.text([width*i+10,10],random.choice(string.ascii_letters),
                  font = Font,fill = (random.randint(1,100),
                                       random.randint(1,100),
                                       random.randint(1,100)))
    im = im.filter(ImageFilter.BLUR)
    im.show()    
        
get_picture()
