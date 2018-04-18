# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from libs.yuntongxin.CCPRestSDK import REST
import ConfigParser

# ���ʺ�
accountSid = '8a216da862cc8f910162d84948c7089f'

# ���ʺ�Token
accountToken = '769e60acf00740c9944930680b8756be'

# Ӧ��Id
appId = '8a216da862cc8f910162d849492208a6'

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP = 'app.cloopen.com'

# ����˿�
serverPort = '8883'

# REST�汾��
softVersion = '2013-12-26'


# ����ģ�����
# @param to �ֻ�����
# @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
# @param $tempId ģ��Id

class CCP(object):
    def __new__(cls, *args, **kwargs):
        # �жϵ�ǰ����û��_instance�������
        if not hasattr(cls, '_instance'):
            obj = super(CCP, cls).__new__(cls, *args, **kwargs)
            # ��ʼ��sdk
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
        for k, v in result.iteritems():

            if k == 'templateSMS':
                for k, s in v.iteritems():
                    print '%s:%s' % (k, s)
            else:
                print '%s:%s' % (k, v)


if __name__ == '__main__':
    CCP().sendtemplatessms(13520616314, ['123456', 2], 1)
