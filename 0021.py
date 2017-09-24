import pymysql
import uuid #用于生成随机数
import hashlib  #加密hash的库 

def GetHushPassword(password):
    salt = uuid.uuid4().hex  #产生一个随机数
    #print(salt)
    hash_password = hashlib.md5(password.encode()+salt.encode()).hexdigest()+":"+salt
    return hash_password

def CheckHushPassword(hash_password,user_password):
    password,salt = hash_password.split(":")
    if password == hashlib.md5(user_password.encode()+salt.encode()).hexdigest():
        return 0
    else:
        return 1

def main():
    password1 = input("请输入密码：")
    hash_password = GetHushPassword(password1)
    print("该密码经加密后为："+hash_password)
    password2 = input("请再次输入密码：")
    while CheckHushPassword(hash_password,password2):
        password2 = input("匹配失败，请重新输入：")
    print("匹配成功")
    connect = pymysql.Connect(
          user='root',
          password='lby0525',
          db='test',
          charset='utf8',
          )
    cursor = connect.cursor()
    cursor.execute('create table password (password varchar(20) primary key,hash_password varchar(150))')
    cursor.execute('insert into password (password,hash_password) values(%s,%s)',[str(password1),str(hash_password)])
    connect.commit()
    cursor.close()
    print("已储存到数据库")

main()
