#在图片的任意位置添加字符

from PIL import Image, ImageDraw, ImageFont, ImageFilter

def Image_Draw():
    text = str(input("请输入想要插入的文本:"))
    path = str(input("请输入图片所在路径:"))
    color = str(input("请输入文本的颜色:"))
    Font = int(input("请输入文本的大小:"))
    im = Image.open(path)
    width,height = im.size
    draw = ImageDraw.Draw(im)
    FONT = ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf",Font)
    draw.text([width-80,40],text,font = FONT,fill = color)
    im.show()
    im.save("D:/1.jpg",'jpeg')

IM = Image_Draw()
IM.start()

