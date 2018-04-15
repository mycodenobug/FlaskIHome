# *_*coding:utf-8 *_*
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session

import redis

app = Flask(__name__)

app.config.from_object(Config)

# app.secret_key # 也可以设置SECRET_KEY

db = SQLAlchemy(app)

redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

CSRFProtect(app)

Session(app)
