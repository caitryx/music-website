# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 14:51
version: python 3.9.2
description: 
"""
from sanic import Blueprint

from .user import bp_user, UserInfoView
from .song_list import bp_song_list, SongListView
from .list_song import bp_list_song, ListSongView

# user路由
bp_user.add_route(UserInfoView.as_view(), uri='/')

# song list路由
bp_song_list.add_route(SongListView.as_view(), uri='/')
bp_song_list.add_route(SongListView.style, uri='/style/detail')

# list song路由
bp_list_song.add_route(ListSongView.as_view(), uri='/detail')


# 蓝图组
bp_group = Blueprint.group(bp_user, bp_song_list, bp_list_song)