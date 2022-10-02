# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/10/1 10:14
version: python 3.9.2
description: 
"""
from webargs import fields
from marshmallow import Schema, validate


class PaginationSchema(Schema):
    offset = fields.Int(load_default=0, validate=[validate.Range(min=0)])
    limit = fields.Int(load_default=10, validate=[validate.Range(min=10, max=30)])