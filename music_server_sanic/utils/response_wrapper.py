# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/14 10:29
version: python 3.9.2
description: 
"""


def success_wrapper(data=None, message='成功', code=200):
    """
        包装成功的返回信息
    :param data:
    :param message:
    :param code:
    :return:
    """
    return {
        'data': data,
        'message': message,
        'code': code,
        'success': True,
        'type': 'success'
    }


def warning_wrapper(message='警告', code=400):
    """
        包装出现异常时返回的警告信息
    :param message:
    :param code:
    :return:
    """
    return {
        'code': code,
        'data': None,
        'success': False,
        'message': message,
        'type': 'warning'
    }


def success_wrapper_pagination(data=None, count=0, message='成功', code=200):
    """
        将返回数据进行包装，此函数适用于分页数据。
    :param data:
    :param message:
    :param code:
    :param count: 数据总数量
    :return:
    """
    return {
        'data': data,
        'message': message,
        'code': code,
        'success': True,
        'type': 'success',
        'count': count
    }
