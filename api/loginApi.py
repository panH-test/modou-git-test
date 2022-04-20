#@Author:Hanpan
#@Time:2022/4/20  15:32
#@File:loginApi.py

from config import IP,HEADERS
from tools.logger import GetLog
log = GetLog().get_logger()


class MdwebLogin:
    def __init__(self):
        self.url = IP+'/login'
        log.info(f'登录的url地址：{self.url}')

    def login(self,session,data):
        log.info(f'登录用的data数据是：{data}')
        resp_login = session.post(self.url,json=data,header=HEADERS)
        log.info(f'登录的响应数据：{resp_login}')
        return resp_login

    def login_success(self,session):
        data = {'phoneNumber':'13215943607','smsCode':'123456','ctype':'1'}
        resp_login = session.post(self.url,json=data,header=HEADERS)
        return resp_login