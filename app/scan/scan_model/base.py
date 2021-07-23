# -*- coding: utf-8 -*- 
# @Time : 2021/7/1 15:07 
# @Author : Dotao
# @File : base.py
import hashlib

from app.common_func import load_conf


class BaseScanModel(object):
    '''
    Base ATVirus Software
    '''

    def __init__(self, scan_software, scan_file):
        self.file_path = scan_file
        self.at_virus_process = load_conf(scan_software)

    def get_file_md5(self):
        '''
        get md5 from file
        :param file_path:
        :return:
        '''
        md5_hash = hashlib.md5()
        with open(self.file_path, "rb") as a_file:
            content = a_file.read()
            md5_hash.update(content)
            digest = md5_hash.hexdigest()
        return digest


