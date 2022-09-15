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
        "origins": ['http://localhost:9001'],
        "methods": ["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE"]
    }
