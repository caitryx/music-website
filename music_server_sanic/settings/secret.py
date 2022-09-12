# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/12 10:16
version: python 3.9.2
description: 
"""
from sanic.config import Config


class SecretSetting(Config):
    TESTING = True
