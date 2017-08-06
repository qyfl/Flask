# -*- coding:utf-8 -*-

__author__ = "qyfl"
__date__ = "2017/7/31 0031"

import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# 会员
class User(db.Model):
    __tablename__ = 'user'
    # 编号
    id = db.Column(db.INTEGER, primary_key=True)
    # 昵称
    name = db.Column(db.String(100), unique=True)
    # 密码
    pwd = db.Column(db.String(100))
    # 邮箱
    email = db.Column(db.String(100), unique=True)
    # 手机号码
    phone = db.Column(db.String(11), unique=True)
    # 简介
    info = db.Column(db.Text)
    # 头像
    face = db.Column(db.String(255), unique=True)
    # 注册时间
    addtime = db.Column(db.DATETIME, index=True, default=datetime.utcnow)
    # 唯一标识符
    uuid = db.Column(db.String(255), unique=True)
    # 会员日志外键关系
    userlogs = db.relationship('UserLog', backref='User')
    
    def __repr__(self):
        return '<User %r>' % self.name


# 会员日志
class UserLog(db.Model):
    __tablename__ = 'userlog'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 所属会员
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    # 登录IP
    ip = db.Column(db.String(100))
    # 登录时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return '<UserLog %r>' % self.id

# 标签
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)