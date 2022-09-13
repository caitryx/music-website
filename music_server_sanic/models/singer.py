# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 10:29
version: python 3.9.2
description: 
"""
from tortoise import fields, Model


class Singer(Model):
    id = fields.IntField(pk=True, )
    name = fields.CharField(max_length=45, )
    sex = fields.BooleanField(null=True, )
    pic = fields.CharField(max_length=255, null=True, )
    birth = fields.DatetimeField(null=True, )
    location = fields.CharField(max_length=45, null=True, )
    introduction = fields.CharField(max_length=255, null=True, )

    class Meta:
        table = "singer"
