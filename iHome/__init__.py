# *_*coding:utf-8 *_*
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session
import redis
from config import config_dict

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    config = config_dict[config_name]

    app.config.from_object(config)

    # app.secret_key # 也可以设置SECRET_KEY

    # db = SQLAlchemy(app)

    db.init_app(app)

    redis_store = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)

    CSRFProtect(app)

    Session(app)
    # 可以在register里面指定 url_prefix(名字必须为url_prefix) 默认为'/'
    # 为了防止网址的冲突可以使用 url_for(名字不固定),定位到指定函数
    # 蓝图要在注册时导入,否则可能会出现循环导入
    from api_1_0 import api
    app.register_blueprint(api, url_for='api.index')

    return app
