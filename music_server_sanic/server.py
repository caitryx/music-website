# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/12 10:02
version: python 3.9.2
description: 
"""
from sanic import Sanic

from settings.base import BaseSetting


app = Sanic('yin_music', config=BaseSetting())
try:
    st = __import__('settings.secret', fromlist=('secret',))
    app.update_config(st.SecretSetting)
except ModuleNotFoundError:
    # raise Exception('由于secret模块不存在，所以必须完善settings.base下的配置信息')
    pass
