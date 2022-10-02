# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/10/2 11:12
version: python 3.9.2
description: 
"""
from sanic import Blueprint
from sanic.response import json
from sanic.views import HTTPMethodView
from webargs_sanic.sanicparser import use_args

from validator.list_song import ListSongSchema
from models.song_list import ListSong
from utils.response_wrapper import success_wrapper

bp_list_song = Blueprint('list_song', url_prefix='/listSong')


class ListSongView(HTTPMethodView):
    """
        歌单详细信息
    """
    @use_args(ListSongSchema(), location='query')
    async def get(self, request, args):
        """
            获取歌单中的歌曲列表
        :param request:
        :return:
        """
        songs = await ListSong.filter(song_list_id=args['song_list_id'])
        data = ListSongSchema(many=True).dump(songs)
        return json(success_wrapper(data))
