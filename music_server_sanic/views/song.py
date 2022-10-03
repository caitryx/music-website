# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/10/3 10:02
version: python 3.9.2
description: 
"""
from webargs import fields
from marshmallow import Schema


class SongInfoSchema(Schema):
    id = fields.Int()
    introduction = fields.Str()
    lyric = fields.Str()
