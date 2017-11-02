from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from blog.main import register
from .main import api

db = SQLAlchemy()

def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    config_obj.init_app(app)
    db.init_app(app)
    # attach routes and custom error pages here
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(register, url_prefix='/register')

    return app