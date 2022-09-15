# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 14:51
version: python 3.9.2
description: 
"""
from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import json
from webargs_sanic.sanicparser import use_args
from tortoise.exceptions import IntegrityError

from validator.user import UserInfoSchema, UserDetailSchema
from models.user import Consumer
from utils.response_wrapper import success_wrapper, warning_wrapper


bp_user = Blueprint('user', url_prefix='/user')


class UserInfoView(HTTPMethodView):
    """
        普通用户的业务处理
    """
    @use_args(UserInfoSchema(), location='form')
    async def post(self, request, args):
        """
            登录
        :param request:
        :param args:
        :return:
        """
        user = await Consumer.get_or_none(**args)
        data = success_wrapper([UserInfoSchema().dump(user)], '登录成功')
        return json(data)

    @staticmethod
    @use_args(UserDetailSchema(), location='form')
    async def register(request, args):
        """
            用于注册
            TODO: 后期可以将验证用户名是否已经存在单独做成一个接口，使得前端在未进行表单提交前就可以知道用户名是否已经被注册
        :param request:
        :param args:
        :return:
        """
        try:
            user = await Consumer.create(**args)
        except IntegrityError:
            return json(warning_wrapper('用户名已注册'))
        return json(success_wrapper(None, '注册成功'))
