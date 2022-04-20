import base64
import hashlib


class Secret(object):
    '''
    实现加密方法
    '''
    def __init__(self,string):
        '''
        先对字符串encode()
        '''
        self._string = string.encode('utf-8')

    def md5(self):
        '''
        md5加密
        :return:
        '''
        try:
            sign = hashlib.md5(self._string).hexdigest()
            return sign
        except:
            return False

    def sha1(self):
        '''
        sha1算法封装
        :return:
        '''
        try:
            sign = hashlib.sha1(self._string).hexdigest()
            return sign
        except:
            return False

    def base64encode(self):
        '''
        base64编码方法封装
        :return:
        '''
        try:
             return base64.b64encode(self._string).decode('utf-8')
        except:
            return False


    def base64decode(self):
        '''
        base64解码方法封装
        :return:
        '''
        try:
             return base64.b64decode(self._string).decode('utf-8')
        except:
            return False



