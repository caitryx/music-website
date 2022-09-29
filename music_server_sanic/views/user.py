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
from tortoise.exceptions import IntegrityError, OperationalError
from sanic_jwt_extended.decorators import jwt_required

from validator.user import UseRegisterSchema, UserDetailSchema, UserResetPasswordSchema
from models.user import Consumer
from utils.response_wrapper import success_wrapper, warning_wrapper


bp_user = Blueprint('user', url_prefix='/user')

# sanic-jwt模块所需内容，后期进行删除
# class UserLoginHandler(AuthenticateEndpoint):
#     """
#         jwt的登录处理，本质上也是一个类视图
#     """
#     async def options(self, request, *args, **kwargs):
#         return text('', status=204)
#
#     async def post(self, request, *args, **kwargs):
#         """
#             登录验证
#         :param request:
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         request, args, kwargs = await self.do_incoming(request, args, kwargs)
#
#         config = self.config
#         user = await utils.call(
#             self.instance.ctx.auth.authenticate, request, *args, **kwargs
#         )
#
#         access_token, output = await self.responses.get_access_token_output(
#             request, user, self.config, self.instance
#         )
#
#         if config.refresh_token_enabled():
#             refresh_token = await utils.call(
#                 self.instance.ctx.auth.generate_refresh_token, request, user
#             )
#             output.update({config.refresh_token_name(): refresh_token})
#         else:
#             refresh_token = None
#
#         output.update(
#             self.responses.extend_authenticate(
#                 request,
#                 user=user,
#                 access_token=access_token,
#                 refresh_token=refresh_token,
#             )
#         )
#
#         output = await self.do_output(output, user)
#
#         resp = self.responses.get_token_response(
#             request,
#             access_token,
#             output,
#             refresh_token=refresh_token,
#             config=self.config,
#         )
#
#         return await self.do_response(resp)
#
#     async def do_output(self, output, user):
#         """
#             处理响应内容
#         :param output:
#         :param user:
#         :return:
#         """
#         data = success_wrapper([UserInfoSchema().dump(user)], '登录成功')
#         output.update(data)
#         return output



class UserInfoView(HTTPMethodView):
    """
        普通用户的业务处理
    """

    # @inject_user()
    # @protected()
    @jwt_required
    async def get(self, request, token):
        """
            查询当前用户信息
        :param request:
        :return:
        """
        user_id = token.sub['user_id']
        user = await Consumer.get_or_none(id=user_id)
        data = UserDetailSchema().dump(user)
        return json(success_wrapper([data], ''))

    @use_args(UseRegisterSchema(), location='form')
    async def post(self, request, args):
        """
            用户注册
            TODO: 后期可以将验证用户名是否已经存在单独做成一个接口，使得前端在未进行表单提交前就可以知道用户名是否已经被注册
        :param request:
        :param args:
        :return:
        """
        try:
            user = await Consumer.create(**args)
        except IntegrityError as e:
            return json(warning_wrapper('注册信息重复，一个手机号、邮箱、用户名都只能对应一个用户!'))
        return json(success_wrapper(None, '注册成功'))

    @jwt_required()
    @use_args(UserDetailSchema(), location='form')
    async def put(self, request, args, token):
        """
            修改用户信息
        :param request: sanic request
        :param args: webargs validated data
        :param token: jwt token
        :return:
        """
        user_id = token.sub['user_id']
        user = await Consumer.filter(id=user_id).update(**args)  # 返回更新数量
        if not user:
            return json(warning_wrapper('修改信息失败'))
        return json(success_wrapper(message='修改信息成功'))

    @jwt_required()
    @use_args(UserResetPasswordSchema(), location='form')
    async def patch(self, request, args, token):
        """
            修改用户密码
        :param request:
        :param args:
        :param token:
        :return:
        """
        user_id = token.sub['user_id']
        try:
            user = await Consumer.filter(id=user_id, password=args['old_password']).update(password=args['password'])
        except OperationalError:
            return json(warning_wrapper('修改失败!'))
        except Exception:
            return json(warning_wrapper('修改失败'))
        if not user:
            return json(warning_wrapper('密码不正确!'))
        return json(success_wrapper(message='修改信息成功'))

