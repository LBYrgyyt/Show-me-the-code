#改变一个文件夹中所有照片的分辨率，并保存为另外的文件

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
def change(path):
    count = 10
    width = int(input("请输入宽："))
    height = int(input("请输入高："))
    for file in os.listdir(r"D:\photo"):  #file是文件夹中文件的名称
        im = Image.open(path+"\\"+str(file))
        im.thumbnail((width,height))
        im.save(path+"\\"+str(count)+".jpg",'jpeg')
        count += 1

change("D:\photo")
