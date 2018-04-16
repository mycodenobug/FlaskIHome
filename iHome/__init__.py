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

    return app
