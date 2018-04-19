# *_*coding:utf-8 *_*
from . import api
from flask import request

__author__ = 'Wang'
__time__ = '2018/04/18 下午9:58'


@api.route('/register', methods=['POST'])
def register ():
    mobile = request.form.get('mobile')
    imagecode = request.form.get('imagecode')
    phonecode = request.form.get('phonecode')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    # 获取数据
    # 验证数据的有效性
    # 验证证是不是手机号
    # 因为要用到redis所以try
    # 查询redis中存贮的imagecode和phonecode
    # 校验imagecode, phonecode
    # 验证两次密码是否一致
    # 校验全部通过, 将用户数据存储到数据库,重定向到首页

    return
