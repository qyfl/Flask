# -*- coding:utf-8 -*-

__author__ = "qyfl"
__date__ = "2017/7/31"

from flask import Blueprint

home = Blueprint('home', __name__)
import app.home.views
