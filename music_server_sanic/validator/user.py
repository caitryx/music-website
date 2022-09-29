# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 14:59
version: python 3.9.2
description: 
"""
from webargs import fields
from marshmallow import Schema, validate, EXCLUDE

from .fields import Mobile


class UserInfoSchema(Schema):
    """
        目前用于用户登录参数验证
    """
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

    class Meta:
        additional = ('id', 'avator')
        dump_only = ('avator', 'id')


class UserDetailSchema(Schema):
    """
        用户详细信息
    """
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    birth = fields.Date(required=True)
    phoneNum = fields.Str(attribute='phone_num')
    sex = fields.Int()
    avator = fields.Str(dump_only=True)

    class Meta:
        unknown = EXCLUDE
        additional = ['email', 'introduction', 'location']


class UseRegisterSchema(Schema):
    """
        目前用于用户注册参数验证
    """
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    sex = fields.Int(required=True, validate=[validate.Range(min=0, max=2)])
    phone_num = Mobile()
    email = fields.Email()
    birth = fields.Date(required=True)
    introduction = fields.Str()
    location = fields.Str()


class UserResetPasswordSchema(Schema):
    """
        修改密码参数参政
    """
    old_password = fields.Str(required=True)
    password = fields.Str(required=True)

    class Meta:
        unknown = EXCLUDE
