# -*- coding:utf-8 -*-

__author__ = "qyfl"
__date__ = "2017/7/31"

from . import admin


@admin.route('/')
def index():
    return '<h1 style="color:red">hello,world admin</h1>'