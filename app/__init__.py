# -*- coding: utf-8 -*- 
# @Time : 2021/6/30 13:57 
# @Author : Dotao
# @File : __init__.py.py

from flask import Flask

URL_PREFIX = '/AtVirus/api/v1/engine'


def create_app():
    '''
    init flask app
    :return:
    '''
    app = Flask(__name__, static_folder="./static/", template_folder="./static/", static_url_path="")

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.scan.kaspersky import anti_virus_blue as kaspersky_blueprint
    app.register_blueprint(kaspersky_blueprint, url_prefix=URL_PREFIX)

    return app
