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


# user路由
bp_user.add_route(UserInfoView.as_view(), uri='/')

# song list路由
bp_song_list.add_route(SongListView.as_view(), uri='/')
bp_song_list.add_route(SongListView.style, uri='/style/detail')
# bp_song_list.add_route(SongListDetail.as_view(), uri='/<songlist_id:int>/')
bp_song_list.add_route(SongListDetail.songs, uri='/<songlist_id:int>/songs')


# 蓝图组
bp_group = Blueprint.group(bp_user, bp_song_list)
