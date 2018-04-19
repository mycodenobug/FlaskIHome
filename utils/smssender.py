# coding=utf-8

# -*- coding: UTF-8 -*-

from libs.yuntongxin.CCPRestSDK import REST
import ConfigParser

# 主帐号
accountSid = '8a216da862cc8f910162d84948c7089f'

# 主帐号Token
accountToken = '769e60acf00740c9944930680b8756be'

# 应用Id
appId = '8a216da862cc8f910162d849492208a6'

# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'


# 发送模板短信
# @param to 手机号码
# @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
# @param $tempId 模板Id

class CCP(object):
    def __new__(cls, *args, **kwargs):
        # 判断当前类有没有_instance这个对象
        if not hasattr(cls, '_instance'):
            obj = super(CCP, cls).__new__(cls, *args, **kwargs)
            # 初始化sdk
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)
            cls._instance = obj
        return cls._instance

    # def __init__(self, to, datas, tempId):
    #     self.rest = REST(serverIP, serverPort, softVersion)
    #     self.rest.setAccount(accountSid, accountToken)
    #     self.rest.setAppId(appId)
    #
    def sendtemplatessms(self, to, datas, tempId):
        result = self.rest.sendTemplateSMS(to, datas, tempId)
        print result.get('statusCode')
        if result.get('statusCode') == '000000':
            return 1
        else:
            return 0


# if __name__ == '__main__':
#     mobile = 13520616314
#     mobile = 13562493856
#     sms_cod = 123456
#     try:
#         a = CCP().sendtemplatessms(mobile, [sms_cod, '5'], 1)
#     except Exception as e:
#         print u'短信验证码发送失败'
#         raise
#     if mobile == 000000:
#         print u'短信发送成功'
#     else:
#         print u'短信验证码发送失败'
#     print type(a)
#     print a
