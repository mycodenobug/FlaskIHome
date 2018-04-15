# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import redis


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@192.168.147.3:3306/ihome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    SECRET_KEY = '6s9QxfpgdAfDrHuExnHKurQtadXJzVhzqiLan0erOxBks/Tj+2ujZtjugk48Iy+k'


app = Flask(__name__)

app.config.from_object(Config)

# app.secret_key # 也可以设置SECRET_KEY

db = SQLAlchemy(app)

redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

CSRFProtect(app)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    redis_store.set('name', 'laowang')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
