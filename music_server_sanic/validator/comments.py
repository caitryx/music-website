# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/10/4 10:22
version: python 3.9.2
description: 
"""
from webargs import fields
from marshmallow import Schema

from .user import UserDetailSchema


class CommentInfo(Schema):
    id = fields.Int()
    songListId = fields.Int(attribute='song_list_id')
    type = fields.Int()
    up = fields.Int()
    content = fields.Str()
    createTime = fields.DateTime(attribute='create_time')
    user = fields.Nested(UserDetailSchema(only=('username', 'avator')))
