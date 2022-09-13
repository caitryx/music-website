# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 10:25
version: python 3.9.2
description: 
"""
from tortoise import Model, fields


class Consumer(Model):
    """
        普通用户
    """
    id = fields.IntField(pk=True, )
    username = fields.CharField(unique=True, max_length=255, )
    password = fields.CharField(max_length=100, )
    sex = fields.BooleanField(null=True, )
    phone_num = fields.CharField(unique=True, max_length=15, null=True, )
    email = fields.CharField(unique=True, max_length=50, null=True, )
    birth = fields.DatetimeField(null=True, )
    introduction = fields.CharField(max_length=255, null=True, )
    location = fields.CharField(max_length=45, null=True, )
    avator = fields.CharField(max_length=255, null=True, )
    create_time = fields.DatetimeField()
    update_time = fields.DatetimeField()

    class Meta:
        table = "consumer"


class Admin(Model):
    """
        管理员
    """
    id = fields.IntField(pk=True, )
    name = fields.CharField(unique=True, max_length=45, )
    password = fields.CharField(max_length=45, )

    class Meta:
        table = "admin"
