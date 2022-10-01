# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/30 10:54
version: python 3.9.2
description:
    设置歌单的视图
"""
from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import json
from webargs_sanic.sanicparser import use_args

from models.song_list import SongList
from utils.response_wrapper import success_wrapper
from validator.base import PaginationSchema
from validator.song_list import SongListSchema


bp_song_list = Blueprint('song_list')


class SongListView(HTTPMethodView):

    @use_args(PaginationSchema(), location='headers')
    async def get(self, request, args):
        # 先查询数据中歌单数据数量
        song_list = await SongList.all().offset(args['offset']).limit(args['limit'])
        data = SongListSchema(many=True).dump(song_list)
        return json(success_wrapper(data))
