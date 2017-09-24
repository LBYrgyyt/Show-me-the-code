#找出一个html文件里的所有链接
import requests
from bs4 import BeautifulSoup
import pymysql

def gethtml(url):
    try:
        r=requests.get(html)
        r.raise_for_status()
        r.encoing=r.apprent_encoding
        return r.text
    except:
        return ""

def getlist(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for i in soup.find_all('link'):
        get = i.attrs['href']
        ulist.append(get)
    for i in soup.find_all('div'):
        get = i.find_all('a')
        g = get.attrs['href']
        ulist.append(g)
        
def put_in_mysql(ulist):
    connect = pymysql.Connect(user='root',
                              password='lby0525',
                              db='test',
                              charset='utf8')
    cursor = connect.cursor()
    cursor.execute("create table html (count varchar(5) primary key,h varchar(300))")
    c = 1
    for i in ulist:
        cursor.execute("insert into html (count,h) values(%s,%s)",[str(c),str(i)])
        c = c + 1
    connect.commit()
    cursor.close()

def main():
    ulist = []
    #f.open("html文件",'w+')
    url = 'https://github.com/Show-Me-the-Code/show-me-the-code'
    html = gethtml(url)
    getlist(ulist,html)
    for i in ulist:
        print(i)
    put_in_mysql(ulist)
    print("保存完毕")

main()
