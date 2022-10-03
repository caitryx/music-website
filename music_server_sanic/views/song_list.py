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

from models.song_list import SongList, ListSong
from models.song import Song
from utils.response_wrapper import success_wrapper, success_wrapper_pagination
from validator.base import PaginationSchema
from validator.song_list import SongListSchema, SongStyleSchema


bp_song_list = Blueprint('song_list', url_prefix='/songList')


class SongListView(HTTPMethodView):
    """
        获取歌单相关的信息
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


class SongListDetail(HTTPMethodView):
    """
        获取歌单相关的详细信息
    """
    @staticmethod
    async def songs(request, songlist_id):
        """
            获取
        :param request:
        :param list_id:
        :return:
        """
        # 先查询歌单对应的歌曲id
        song_ids = await ListSong.filter(song_list_id=songlist_id).values_list('song_id', flat=True)
        # 根据歌曲id查询歌曲详情
        songs = await Song.filter(id__in=song_ids).values('id', 'name', 'introduction', 'lyric', 'url')
        return json(success_wrapper(songs))


