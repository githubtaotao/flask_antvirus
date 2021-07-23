# -*- coding: utf-8 -*- 
# @Time : 2021/6/30 14:00 
# @Author : Dotao
# @File : __init__.py.py

from flask import Blueprint

anti_virus_blue = Blueprint('at_virus', __name__)
from . import api
