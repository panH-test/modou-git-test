#@Author:Hanpan
#@Time:2022/4/18  16:39
#@File:testnote.py

'''单功能测试用的草稿本'''
import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456',database='hptest',port=3306)
print(db)
cur = db.cursor()
cur.execute('select * from hp_users')
print(cur.fetchall())
cur.close()
db.close()
