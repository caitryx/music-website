# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/14 10:52
version: python 3.9.2
description: 
"""
from marshmallow import fields, ValidationError
import re


class Mobile(fields.Field):
    """
        自定义手机号验证字段
    """

    def _deserialize(self, value, attr, data, **kwargs):
        """
            反序列化内容，将内容转为python格式数据
        :param value:
        :param attr:
        :param data:
        :param kwargs:
        :return:
        """
        value = value.strip()
        return value

    def _validate(self, value):
        # 使用正则表达式进行验证
        regx = re.compile(r'^1[3-9]\d{9}$')
        res = regx.match(value)
        if not res:
            raise ValidationError('手机号格式不正确!')
        super(Mobile, self)._validate(value)