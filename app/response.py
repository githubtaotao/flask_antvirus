# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 21:41
# @Author  : Dotao

from flask import jsonify


class Response(object):
    '''
    basic response
    '''
    def success(self, data=None):
        return jsonify({'code': 20000, 'msg': 'success!', 'data': data})

    def failed(self, msg='', code=50000):
        return jsonify({'code': code, 'msg': 'error!' + str(msg), 'data': ''})

    def refuse(self, msg=''):
        return jsonify({'code': 40300, 'msg': 'failure!' + str(msg)})
