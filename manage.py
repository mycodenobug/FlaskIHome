# -*- coding: utf-8 -*-
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import redis
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

# app.secret_key # 也可以设置SECRET_KEY

db = SQLAlchemy(app)

redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

CSRFProtect(app)

Session(app)

manage = Manager(app)

Migrate(app, db)

manage.add_command('db', MigrateCommand)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    manage.run()
