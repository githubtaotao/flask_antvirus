# -*- coding: utf-8 -*- 
# @Time : 2021/6/30 14:11 
# @Author : Dotao
# @File : __init__.py.py
from flask import Blueprint

main = Blueprint('main', __name__)
from . import api