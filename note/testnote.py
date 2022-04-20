#@Author:Hanpan
#@Time:2022/4/18  16:39
#@File:testnote.py

'''单功能测试用的草稿本'''
# import pymysql
#
# db = pymysql.connect(host='localhost',user='root',password='123456',database='hptest',port=3306)
# print(db)
# cur = db.cursor()
# cur.execute('select * from hp_users')
# print(cur.fetchall())
# cur.close()
# db.close()

import requests

res = requests.post('https://pcintf.vanturnyijian.com/login',json={'phoneNumber': "13215943607", 'smsCode': "123456", 'ctype': "1"},headers={'Content-Type': 'application/json;charset=UTF-8'})
print(res.json().get('msg'))
