# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 14:51
version: python 3.9.2
description: 
"""
from sanic import Blueprint

from .user import bp_user, UserInfoView

# user路由
bp_user.add_route(UserInfoView.as_view(), uri='/')


# 蓝图组
bp_group = Blueprint.group(bp_user)