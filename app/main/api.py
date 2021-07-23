# -*- coding: utf-8 -*- 
# @Time : 2021/6/30 14:01 
# @Author : Dotao
# @File : api.py
from . import main


@main.route('/')
def index():
    '''

    :return:
    '''
    return 'This is home page, we have nothing to serve.'
