# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 10:25
version: python 3.9.2
description: 
"""
from tortoise import Model, fields
from sanic_jwt.exceptions import AuthenticationFailed


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
    birth = fields.DateField(null=True, )
    introduction = fields.CharField(max_length=255, null=True, )
    location = fields.CharField(max_length=45, null=True, )
    avator = fields.CharField(max_length=255, null=True, )
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "consumer"

    def check_password(self, password):
        """
            检查当前用户对象与传入的密码是否相同
            TODO: 后期需要比对加密的密码
        :param password:
        :return:
        """
        return self.password == password

    def to_dict(self):
        """
            jwt模块会根据返回的内容决定jwt中加密什么内容(user_id是固定写法)
        :return:
        """
        return {"user_id": self.id}

    @staticmethod
    async def authenticate(request, *args, **kwargs):
        """
            验证方法(用于jwt认证)
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            raise AuthenticationFailed('用户名或密码不正确')
        user = await Consumer.filter(username=username).first()
        if not user or not user.check_password(password):
            raise AuthenticationFailed('用户名或密码不正确')
        return user


class Admin(Model):
    """
        管理员
    """
    id = fields.IntField(pk=True, )
    name = fields.CharField(unique=True, max_length=45, )
    password = fields.CharField(max_length=45, )

    class Meta:
        table = "admin"
