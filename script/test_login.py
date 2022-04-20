#@Author:Hanpan
#@Time:2022/4/15  14:50
#@File:test_login.py

import pytest
import requests
import allure
from tools.analyze_data import analyze_data
from api.loginApi import MdwebLogin
# data_li = [
#     ('13215943607','123456','1','成功'),
#     ('13215943607','1','1','验证码输入不正确'),
#     ('','1','1','发送手机号不能为空'),
#     ('13215943607','123456','','ctype错误'),
#     ]
#
# ids = ['正向用例','验证码错误','手机号为空','ctype错误']


@allure.feature('PC项目后台企业端接口测试用例')
class Test_Weblogin:

    def setup_class(self):
        self.session = requests.Session()
        self.login_obj = MdwebLogin()


    @allure.story('登录成功的测试用例')
    def test_login_success(self):
        '''
        登录成功
        :return:
        '''
        resp_login = self.login_obj.login_success(self.session)
        print(resp_login.json())
        assert resp_login.json().get('msg') == "成功"


    @pytest.mark.parametrize('args',analyze_data('login_data','test_login'))
    # @pytest.mark.run(order=1)
    @allure.severity('blocker')
    @allure.title('登录异常，测试数据是：{args}')
    @allure.story('登录失败的测试用例')
    @allure.link('https://pcintf.vanturnyijian.com/login',name='墨斗工约项目后台')

    # @allure.description('登录测试用例')
    def test_login_error(self,args):
        '''
        登录失败
        :return: msg断言
        '''
        # allure.attach('./img/girljpg.jpg', name='萌妹', attachment_type='jpg')

        data = {'phoneNumber':args['phoneNumber'],'smsCode':args['smsCode'],'ctype':args['ctype']}
        resp_login = self.login_obj.login(self.session,data)
        assert resp_login.json().get('msg') == args['exp']


# if __name__ == '__main__':
#     Test_Weblogin.test_login_success()
#     pytest.main(['-sv','test_login.py'])



