# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from config import config
from flask import Flask

# 数据库实例
db = SQLAlchemy()

# Mail
mail = Mail()


# 创建Flask应用实例
def create_app(config_name):

    # 初始化Flask APP
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    # 绑定数据库
    db.init_app(app)

    # 绑定蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app