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
from .base import PaginationSchema
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


class SongStyleSchema(PaginationSchema):
    """
        歌单分类信息。理论上可以将这个合并到SongListSchema中，但是考虑到后期后台管理中可能
        要修改歌单信息，所以单独将分类提取出来。
    """
    style = fields.Str(required=True)
