# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/12 10:06
version: python 3.9.2
description: 
"""
from sanic.config import Config


class BaseSetting(Config):
    # 跨域配置信息
    CORS_OPTIONS = {
        "resources": r'/*',
        "origins": "*",
        "methods": ["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE"]
    }



    # 数据库配置信息(tortoise)
    # DB_CONFIG = {
    #     'connections': {
    #         'default': {
    #             'engine': 'tortoise.backends.mysql',
    #             'credentials': {
    #                 'host': '127.0.0.1',
    #                 'port': '33065',
    #                 'user': 'root',
    #                 'password': '123456',
    #                 'database': 'tp_music',
    #             }
    #         }
    #     },
    #     'apps': {
    #
    #     }
    #
    # }
