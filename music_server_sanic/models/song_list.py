# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 10:30
version: python 3.9.2
description: 
"""
from tortoise import Model, fields

from .song import Comment


class SongList(Model):
    id = fields.IntField(pk=True, )
    title = fields.CharField(max_length=255, )
    pic = fields.CharField(max_length=255, null=True, )
    introduction = fields.TextField(null=True, )
    style = fields.CharField(max_length=10, null=True, default='无', )

    # reverse
    comments: fields.ReverseRelation['Comment']

    class Meta:
        table = "song_list"


class ListSong(Model):
    id = fields.IntField(pk=True, )
    song_id = fields.IntField()
    song_list_id = fields.IntField()

    class Meta:
        table = "list_song"


class RankList(Model):
    id = fields.BigIntField(pk=True, )
    songListId = fields.BigIntField(index=True, )
    consumerId = fields.BigIntField(index=True, )
    score = fields.IntField()

    class Meta:
        table = "rank_list"


class Collect(Model):
    id = fields.IntField(pk=True, )
    user_id = fields.IntField()
    type = fields.BooleanField()
    song_id = fields.IntField()
    song_list_id = fields.IntField()
    create_time = fields.DatetimeField()

    class Meta:
        table = "collect"
