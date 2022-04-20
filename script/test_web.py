#@Author:Hanpan
#@Time:2022/4/15  14:50
#@File:test_web.py

import pytest
import requests
import allure

data_li = [
    ('13215943607','123456','1','成功'),
    ('13215943607','1','1','验证码输入不正确'),
    ('','1','1','发送手机号不能为空'),
    ('13215943607','123456','','ctype错误'),
    ]

ids = ['正向用例','验证码错误','手机号为空','ctype错误']


@allure.feature('PC项目后台企业端接口测试用例')
class Test_webmodou:
    test_ip = 'http://120.92.35.79:9084'
    pro_Ip = 'https://pcintf.vanturnyijian.com'
    header = {'Connect-Type':'application/x-www-form-urlencoded;charset=UTF-8'}

    @pytest.mark.parametrize('phoneNumber,smsCode,ctype,exp', data_li,ids=ids)
    @pytest.mark.run(order=2)
    @allure.severity('blocker')
    @allure.story('登录测试用例')
    @allure.link('https://www.baidu.com',name='百度一下')

    # @allure.description('登录测试用例')
    def test_login(self,phoneNumber,smsCode,ctype,exp):
        '''
        登录测试用例，正向一条，验证码错误一条
        :param phoneNumber: 电话号码
        :param smsCode: 短信验证码
        :param ctype: ctype，1：企业，2：项目
        :param exp: 预期结果
        :return: msg断言
        '''
        allure.attach('./img/girljpg.jpg', name='萌妹', attachment_type='jpg')
        url = self.pro_Ip+'/login'
        data = {'phoneNumber':phoneNumber,'smsCode':smsCode,'ctype':ctype}
        r = requests.post(url,json=data,headers=self.header)
        res =r.json()
        assert res['msg'] == exp

    # @pytest.mark.run(order=1)
    # @allure.severity('blocker')
    # def test_register(self):
    #     pass



# if __name__ == '__main__':
#     Test_webmodou.test_login()
#     pytest.main(['-sv','test_web.py'])


