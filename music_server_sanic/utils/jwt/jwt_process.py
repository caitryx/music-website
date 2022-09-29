# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/25 9:35
version: python 3.9.2
description: 
"""
from sanic_jwt_extended import JWT
from datetime import timedelta

from settings.product import ProdSetting


def jwt_initialize(app):
    """
        初始化jwt
    :param app:
    :return:
    """
    with JWT.initialize(app) as manager:
        manager.config.use_acl = True
        # 设置密钥
        manager.config.secret_key = ProdSetting.JWT_SECRET
        # 设置access token过期时间
        manager.config.access_token_expires = timedelta(days=1)
