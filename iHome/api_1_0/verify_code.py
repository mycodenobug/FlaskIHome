# *_*coding:utf-8 *_*
from . import api
from utils.captcha.captcha import captcha
from flask import request, current_app, jsonify, make_response
from iHome import redis_store, constants
from iHome.constants import IMAGE_CODE_REDIS_EXPIRES
from iHome.response_code import RET

__author__ = 'Wang'
__time__ = '2018/04/18 下午1:06'


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
    print pre
    # 生成验证码
    name, text, image = captcha.generate_captcha()
    # 删除之前验证码并保存当前验证码
    # 保存'验证码'&'uuid'到redis
    # 格式:redis.set(key, value, 过期时间)
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


@api.route('/')
def index():
    # current_app.loger.debug('asdffads')
    return 'ok'
