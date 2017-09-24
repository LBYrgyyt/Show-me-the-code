import pymysql
import random
import string

#show databases;  查看数据库
#create database test;   创建数据库
#use test;  使用数据库

ulist= []

connect = pymysql.Connect(
          user='root',
          password='lby0525',
          db='test',
          charset='utf8',
          )    #打开数据库连接
cursor = connect.cursor()  #获取游标（游标是个什么东西）
#cursor.execute()   #使用execute方法执行SQL语句
#cursor.execute('select * from user where count = %s', ('1',))  查询语句
#update 更新语句
#data = cursor.fetchone()  #使用fetchone方法获取一条数据库
#data = cursor.fetchall()  #使用fetchall方法获取所有数据库
#其余操作详见  http://blog.csdn.net/u011662320/article/details/38390563

cursor.execute('create table code (count varchar(5) primary key,cd varchar(35))')
for i in range(200):
    password = "-".join("".join(random.choice(string.digits+string.ascii_letters))for i in range(30))
    ulist.append(password)
c = 1
for i in ulist:
    cursor.execute('insert into code (count,cd) values(%s,%s)',[str(c),str(i)])
    c = c+1
connect.commit()  #执行操作后要调用commit()提交事务
cursor.close()
