# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/25 9:44
version: python 3.9.2
description: 
"""
from sanic import Blueprint
from sanic_jwt_extended import JWT
from sanic.response import json
from webargs_sanic.sanicparser import use_args

from validator.user import UserInfoSchema
from models.user import Consumer
from utils.response_wrapper import success_wrapper, warning_wrapper


@use_args(UserInfoSchema(), location='form')
async def login(request, args):
    """
        登录获取jwt token(后期需要对其进行权限、refresh token以及封禁的处理，可以参考sanic-jwt的实现)
    :param request:
    :return:
    """
    user = await Consumer.get_or_none(**args)
    if not user:
        return json(warning_wrapper('用户名或密码错误'))
    resp_data = success_wrapper([UserInfoSchema().dump(user)], '登录成功')
    resp_data['access_token'] = JWT.create_access_token({'user_id': user.id}, 'normal')
    return json(resp_data)


bp_jwt = Blueprint('jwt')
bp_jwt.add_route(login, uri='/auth/login', methods=['POST'])