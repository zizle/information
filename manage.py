# _*_ coding:utf-8 _*_

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from datetime import timedelta


class Config(object):
    DEBUG = True
    # 连接数据库MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymsql://root:mysql@127.0.0.1:3306/db_information_github'
    # 设置不追踪数据库改变，提高点性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis 数据库配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # 设置session秘钥
    SECRET_KEY = 'abc'
    # 设置session的存活时间
    PERMANENT_SESSION_LIFETIME = timedelta(days=3)
    # 设置session用什么存储
    SESSION_TYPE = 'redis'
    # 设置session存储在后端的位置
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # session使用秘钥
    SESSION_USE_SIGNER = True


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
CSRFProtect(app)
Session(app)


@app.route('/')
def index():
    return '<h1>hello flask!</h1>'


if __name__ == '__main__':
    app.run()