# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/10/3 11:10
version: python 3.9.2
description: 
"""
from webargs import fields
from marshmallow import Schema

from .fields import URLStringField
from settings.product import ProdSetting


class SongInfoSchema(Schema):
    """
        歌曲详细信息
    """
    url = URLStringField(metadata={'host': ProdSetting.STATIC_RESOURCE_ADDRESS})
    pic = URLStringField(metadata={'host': ProdSetting.STATIC_RESOURCE_ADDRESS})

    class Meta:
        additional = ['id', 'name', 'introduction', 'lyric']