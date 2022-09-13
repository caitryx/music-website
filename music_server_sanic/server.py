# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/12 10:02
version: python 3.9.2
description: 
"""
import sanic.response
from sanic import Sanic
from sanic_ext import Extend
from sanic_cors import CORS
from tortoise.contrib.sanic import register_tortoise

from settings.base import BaseSetting


app = Sanic('yin_music', config=BaseSetting())

# 处理生产配置文件
try:
    st = __import__('settings.product', fromlist=('product',))
    app.update_config(st.ProdSetting)
except ModuleNotFoundError:
    pass

# 注册tortoise
register_tortoise(app, config=app.config.DB_CONFIG)

# 设置跨域
Extend(app, extensions=[CORS], config={'CORS': False, 'CORS_OPTIONS': app.config.CORS_OPTIONS})
