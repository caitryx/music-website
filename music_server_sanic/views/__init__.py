# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 14:51
version: python 3.9.2
description: 
"""
from sanic import Blueprint

from .user import bp_user, UserInfoView
from .song_list import bp_song_list, SongListView, SongListDetail
from .song import bp_song, SongInfoView


# user路由
bp_user.add_route(UserInfoView.as_view(), uri='/')

# song list路由
bp_song_list.add_route(SongListView.as_view(), uri='/')
bp_song_list.add_route(SongListView.style, uri='/style/detail')
bp_song_list.add_route(SongListDetail.songs, uri='/<songlist_id:int>/songs')
bp_song_list.add_route(SongListDetail.comments, uri='/<songlist_id:int>/comments')

# song路由
bp_song.add_route(SongInfoView.comments, uri='/<song_id:int>/comments')


# 蓝图组
bp_group = Blueprint.group(bp_user, bp_song_list, bp_song)
