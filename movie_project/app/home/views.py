# -*- coding:utf-8 -*-

__author__ = "qyfl"
__date__ = "2017/7/31"

from . import home


@home.route('/')
def index():
    return '<h1 style="color:green">hello,world home</h1>'
