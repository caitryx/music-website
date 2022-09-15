# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 14:59
version: python 3.9.2
description: 
"""
from webargs import fields
from marshmallow import Schema, validate

from .fields import Mobile


class UserInfoSchema(Schema):
    """
        目前用于用户登录参数验证
    """
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

    class Meta:
        additional = ('id', 'username', 'avator')
        dump_only = ('avator',)


class UserDetailSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    sex = fields.Int(required=True, validate=[validate.Range(min=0, max=2)])
    phone_num = Mobile()
    email = fields.Email()
    birth = fields.Date(required=True)
    introduction = fields.Str()
    location = fields.Str()