# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/10/1 9:53
version: python 3.9.2
description: 
"""
from webargs import fields
from marshmallow import Schema, validate

from .fields import URLStringField
from settings.product import ProdSetting


class SongListSchema(Schema):
    """
        歌单信息
    """
    id = fields.Int()
    introduction = fields.Str()
    pic = URLStringField(metadata=({'host': ProdSetting.STATIC_RESOURCE_ADDRESS}))
    style = fields.Str()
    title = fields.Str()
