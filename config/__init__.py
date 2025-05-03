import logging

from flask import Flask

from models import db
from routes import all_blueprints
from .mongo_settings import MongoConfig

# Basic config for logging
logging.basicConfig(level=logging.INFO)


def create_app(app_name):
    """
    Create a flask app instance
    :return: Flask app instance
    """
    app = Flask(app_name)
    app.config.from_object(MongoConfig)

    # 虽然只显式创建了一个 MongoEngine 实例 db 并进行了一次 db.init_app(app) 操作
    # 但 MongoEngine 实例会根据 app.config 中的多数据库配置创建多个数据库连接实例
    # 并且通过实体类中的 db_alias 来决定每个类使用哪个数据库连接进行操作。
    db.init_app(app)

    for bp in all_blueprints:
        app.register_blueprint(bp)

    return app
