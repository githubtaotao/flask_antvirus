# -*- coding: utf-8 -*- 
# @Time : 2021/7/1 14:47 
# @Author : Dotao
# @File : common_func.py
import os
import configparser


def load_path():
    '''
    get db filepath
    :return:
    '''
    current_path = os.path.abspath(__file__)
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    return father_path + os.path.sep + "antivirus.conf"


def load_conf(software):
    '''
    get Antivirus software exe
    :param software:
    :return:
    '''
    full_path = load_path()
    cf = configparser.ConfigParser()
    cf.read(full_path)
    return cf.get(software, "absoluteLocation")
