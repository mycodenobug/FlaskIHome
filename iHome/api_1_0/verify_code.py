# *_*coding:utf-8 *_*
from . import api
from utils.captcha.captcha import captcha
from flask import request

__author__ = 'Wang'
__time__ = '2018/04/18 下午1:06'


@api.route('/image_code')
def verify():
    cur = request.args.get('cur')
    print cur
    name, text, image = captcha.generate_captcha()
    print name, text
    return image
