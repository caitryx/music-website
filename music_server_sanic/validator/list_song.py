# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/10/2 11:14
version: python 3.9.2
description: 
"""
from webargs import fields
from marshmallow import Schema, validate


class ListSongSchema(Schema):
    id = fields.Int(dump_only=True)
    songListId = fields.Int(required=True, attribute='song_list_id')
    songId = fields.Int(attribute='song_id')
