# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 14:51
version: python 3.9.2
description: 
"""
from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import json, text
from webargs_sanic.sanicparser import use_args
from tortoise.exceptions import IntegrityError
from sanic_jwt.endpoints import AuthenticateEndpoint
from sanic_jwt import utils

from validator.user import UserInfoSchema, UserDetailSchema
from models.user import Consumer
from utils.response_wrapper import success_wrapper, warning_wrapper


bp_user = Blueprint('user', url_prefix='/user')


class UserLoginHandler(AuthenticateEndpoint):
    """
        jwt的登录处理，本质上也是一个类视图
    """
    async def options(self, request, *args, **kwargs):
        return text('', status=204)

    async def post(self, request, *args, **kwargs):
        """
            登录验证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        request, args, kwargs = await self.do_incoming(request, args, kwargs)

        config = self.config
        user = await utils.call(
            self.instance.ctx.auth.authenticate, request, *args, **kwargs
        )

        access_token, output = await self.responses.get_access_token_output(
            request, user, self.config, self.instance
        )

        if config.refresh_token_enabled():
            refresh_token = await utils.call(
                self.instance.ctx.auth.generate_refresh_token, request, user
            )
            output.update({config.refresh_token_name(): refresh_token})
        else:
            refresh_token = None

        output.update(
            self.responses.extend_authenticate(
                request,
                user=user,
                access_token=access_token,
                refresh_token=refresh_token,
            )
        )

        output = await self.do_output(output, user)

        resp = self.responses.get_token_response(
            request,
            access_token,
            output,
            refresh_token=refresh_token,
            config=self.config,
        )

        return await self.do_response(resp)

    async def do_output(self, output, user):
        """
            处理想用内容
        :param output:
        :param user:
        :return:
        """
        data = success_wrapper([UserInfoSchema().dump(user)], '登录成功')
        output.update(data)
        return output



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
