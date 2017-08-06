# -*- coding:utf-8 -*-

__author__ = "qyfl"
__date__ = "2017/7/31"

from flask import Blueprint

admin = Blueprint('admin', __name__)
import app.admin.views
