# *_*coding:utf-8 *_*
import redis


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@192.168.147.3:3306/ihome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    SECRET_KEY = '6s9QxfpgdAfDrHuExnHKurQtadXJzVhzqiLan0erOxBks/Tj+2ujZtjugk48Iy+k'
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400 * 2


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@192.168.147.3:3306/ihome'


config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig

}
