# -*- coding: utf-8 -*- 
# @Time : 2021/6/30 14:01 
# @Author : Dotao
# @File : api.py

import traceback

from flask import request

from app.response import Response as MyResponse
from . import anti_virus_blue as kaspersky
from .service import scan_file

rsp = MyResponse()


@kaspersky.route('/kaspersky/file', methods=["GET"])
def route_scan_file():
    '''
    scan file
    :param file_path:
    :return:
    '''
    try:
        args = request.args.get("file_path")
        rst = scan_file(args)
        return rsp.success(rst)
    except Exception as e:
        traceback.print_exc()
        return rsp.failed(e)
