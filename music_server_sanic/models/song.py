# -*- coding: utf-8 -*-
"""
@Author: Mno
@Date: 2022/9/13 10:28
version: python 3.9.2
description: 
"""
from tortoise import fields, Model


class Song(Model):
    id = fields.IntField(pk=True, )
    singer_id = fields.IntField()
    name = fields.CharField(max_length=45, )
    introduction = fields.CharField(max_length=255, null=True, )
    create_time = fields.DatetimeField(description='发行时间', )
    update_time = fields.DatetimeField()
    pic = fields.CharField(max_length=255, null=True, )
    lyric = fields.TextField(null=True, )
    url = fields.CharField(max_length=255, )

    # reverse
    comments: fields.ReverseRelation['Comment']

    class Meta:
        table = "song"


class Comment(Model):
    id = fields.IntField(pk=True, )
    # user_id = fields.IntField()
    user = fields.ForeignKeyField('models.Consumer', source_fields='user_id', related_name='comments', on_delete=fields.CASCADE)
    # song_id = fields.IntField()
    song = fields.ForeignKeyField('models.Song', source_fields='song_id', related_name='comments',
                                  on_delete=fields.CASCADE)
    # song_list_id = fields.IntField()
    song_list = fields.ForeignKeyField('models.SongList', source_fields='song_list_id', related_name='comments',
                                       on_delete=fields.CASCADE)
    content = fields.CharField(max_length=255, null=True, )
    create_time = fields.DatetimeField(null=True, )
    type = fields.BooleanField()
    up = fields.IntField()

    class Meta:
        table = "comment"
