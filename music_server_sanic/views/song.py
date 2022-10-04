# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/10/4 11:03
version: python 3.9.2
description: 
"""
from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import json

from models.song import Song
from validator.comments import CommentInfo
from utils.response_wrapper import success_wrapper


bp_song = Blueprint('song', url_prefix='/song')


class SongInfoView(HTTPMethodView):
    @staticmethod
    async def comments(request, song_id):
        """
            获取歌曲评论
        :param request:
        :param song_id:
        :return:
        """
        song = await Song.get_or_none(id=song_id).prefetch_related('comments')
        comments = await song.comments.all().prefetch_related('user')
        data = CommentInfo(many=True).dump(comments)
        return json(success_wrapper(data))
