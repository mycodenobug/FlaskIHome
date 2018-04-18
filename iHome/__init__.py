# *_*coding:utf-8 *_*
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session
import redis
from config import config_dict
# from web_html import RegexConverter # 废弃物
from utils.commons import RegexConverter
import logging
from logging.handlers import RotatingFileHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db = SQLAlchemy()

redis_store = None


def LogConfig(log_level):
    # 设置日志的记录等级
    logging.basicConfig(level=log_level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler(BASE_DIR + "/logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    app = Flask(__name__)

    config = config_dict[config_name]

    app.config.from_object(config)

    LogConfig(config.log_level)

    # app.secret_key # 也可以设置SECRET_KEY

    # db = SQLAlchemy(app)

    db.init_app(app)

    global redis_store

    redis_store = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)

    CSRFProtect(app)

    Session(app)
    app.url_map.converters['re'] = RegexConverter
    # 可以在register里面指定 url_prefix(名字必须为url_prefix) 默认为'/'
    # 为了防止网址的冲突可以使用 url_for(名字不固定),定位到指定函数
    # 蓝图要在注册时导入,否则可能会出现循环导入
    from api_1_0 import api
    # app.register_blueprint(api, url_for='api.index')
    app.register_blueprint(api, url_prefix='/api/v1_0')

    import web_html
    app.register_blueprint(web_html.html)

    return app
