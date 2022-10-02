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
from utils.response_wrapper import success_wrapper, success_wrapper_pagination
from validator.base import PaginationSchema
from validator.song_list import SongListSchema, SongStyleSchema


bp_song_list = Blueprint('song_list', url_prefix='/songList')


class SongListView(HTTPMethodView):
    """
        获取歌单列表
    """

    @use_args(PaginationSchema(), location='query')
    async def get(self, request, args):
        # 查询数据总量
        count = await SongList.all().count()
        # 先查询数据中歌单数据数量
        song_list = await SongList.all().offset(args['offset']).limit(args['limit'])
        data = SongListSchema(many=True).dump(song_list)
        return json(success_wrapper_pagination(data,  count))

    @staticmethod
    @use_args(SongStyleSchema(), location='query')
    async def style(request, args):
        """
            获取指定分类的歌单信息
        :param request:
        :return:
        """
        count = await SongList.filter(style__contains=args['style']).count()
        song_list = await SongList.filter(style__contains=args['style']).offset(args['offset']).limit(args['limit'])
        data = SongListSchema(many=True).dump(song_list)
        return json(success_wrapper_pagination(data, count))


# class ListSongView(HTTPMethodView):
#     """
#         歌单详细信息
#     """
#     @use_args(ListSongSchema(), location='query')
#     async def get(self, request, args):
#         """
#             获取歌单中的歌曲列表
#         :param request:
#         :return:
#         """
#         songs = await ListSong.filter(song_list_id=args['song_list_id'])
#         return json(success_wrapper(ListSongSchema().dump(songs)))


