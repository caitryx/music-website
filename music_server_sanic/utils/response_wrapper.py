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


def warning_wrapper(message='警告'):
    """
        包装出现异常时返回的警告信息
    :param message:
    :return:
    """
    return {
        'code': 400,
        'data': None,
        'success': False,
        'message': message,
        'type': 'warning'
    }
