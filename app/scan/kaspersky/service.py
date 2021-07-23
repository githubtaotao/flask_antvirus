# -*- coding: utf-8 -*- 
# @Time : 2021/7/1 15:37 
# @Author : Dotao
# @File : service.py
from .kaspersky import Kaspersky


def scan_file(path):
    '''
    scan file
    :param path:
    :return:
    '''
    kas = Kaspersky('Kaspersky', path)
    rst = kas.scan()
    return rst
