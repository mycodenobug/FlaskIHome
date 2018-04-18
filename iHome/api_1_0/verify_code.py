# *_*coding:utf-8 *_*
from . import api
from utils.captcha.captcha import captcha
from flask import request, current_app, jsonify, make_response
from iHome import redis_store, constants
from iHome.constants import IMAGE_CODE_REDIS_EXPIRES
from iHome.response_code import RET
import json
import re

__author__ = 'Wang'
__time__ = '2018/04/18 下午1:06'


@api.route('/sms_code', methods=['POST'])
def sms_code():
    # json局部刷新
    # 获取手机号, 验证码, 验证码id
    # 判断数据是否存在
    # 判断是否是手机号
    # 判断验证码是否正确
    # 从redis中查询数据, 如果查询出错返回错误信息
    # 如果没有查到数据返回错误信息
    # 判断验证码是否存在 不存在返回错误信息
    # 判断验证码是否输入正确, 不正确返回错误信息
    # 因为下面要用到第三方接口所以要try一下
    # 调用接口, 发送短信 验证码
    # 如果出错返回errno: & errmsg:
    # 返回状态信息

    # 获取手机号, 验证码

    # 获取手机号, 验证码
    req_data = request.data
    req_dic = json.loads(req_data)
    mobile = req_dic.get('mobile')
    imageCode = req_dic.get('imageCode')
    imageId = req_dic.get('imageId')
    # 判断数据是否存在
    if not all([mobile, imageCode, imageId]):
        return jsonify(errno=RET.DATAERR, errmsg=u'数据不完整')
    # 判断是否是手机号
    if not re.match(r'1[3456789]\d{9}', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg=u'手机号错误')
    # 判断验证码是否正确
    # 从redis中查询数据, 如果查询出错返回错误信息
    try:
        red_data = redis_store.get('image_code:%s' % imageId)
    except Exception as e:
        current_app.logger.error(u'查不到数据')
        return jsonify(errno=RET.NODATA, errmsg=u'查询验证码失败')
    # 如果没有查到数据, 验证码不存在
    if not red_data:
        return jsonify(errno=RET.DBERR, errmsg=u'验证码过期')
    # 判断验证码是否输入正确, 不正确返回错误信息
    if red_data != imageCode:
        return jsonify(errno=RET.DATAERR, errmsg=u'验证码输入错误')
    # 调用接口, 发送短信 验证码
    # 如果出错返回errno: & errmsg:

    return jsonify(errno=RET.OK, errmsg=u'短信发送成功')


@api.route('/image_code')
def verify():
    # 获取参数:uuid
    # 生成验证码
    # 删除之前验证码并保存当前验证码
    # 保存'验证码'&'uuid'到redis
    # 返回验证码

    # 获取参数:uuid
    cur = request.args.get('cur')
    pre = request.args.get('pre')
    # 生成验证码
    name, text, image = captcha.generate_captcha()
    # 删除之前验证码并保存当前验证码
    # 保存'验证码'&'uuid'到redis
    # 格式:redis.set(key, value, 过期时间)
    print '验证码:', text
    try:
        if pre != '':
            redis_store.delete('image_code:%s' % pre)
        redis_store.set('image_code:%s' % cur, text, IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存验证码失败')
    # 返回验证码
    res = make_response(image)
    # 修改响应的类型
    res.headers['Content-Type'] = 'image/jpg'
    return res
