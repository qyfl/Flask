# -*- coding:utf-8 -*-

__author__ = "qyfl"
__date__ = "2017/7/31 0031"

from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# 用户
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
    # 用户日志外键关系
    userlogs = db.relationship('UserLog', backref='user')
    # 评论外键关系
    comments = db.relationship('Comment', backref='user')
    # 收藏外键关系
    moviecols = db.relationship('Moviecol', backref='user')
    
    def __repr__(self):
        return '<User %r>' % self.name


# 用户日志
class UserLog(db.Model):
    __tablename__ = 'userlog'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 所属用户
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 登录IP
    ip = db.Column(db.String(100))
    # 登录时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return '<UserLog %r>' % self.id


# 标签
class Tag(db.Model):
    __tablename__ = 'tag'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 标题
    name = db.Column(db.String(100), unique=True)
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # 电影外键关系关联
    movies = db.relationship('Movie', backref='tag')
    
    def __repr__(self):
        return '<Tag %r>' % self.name


# 电影
class Movie(db.Model):
    __tablename__ = 'movie'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 标题
    title = db.Column(db.String(255), unique=True)
    # 地址
    url = db.Column(db.String(255), unique=True)
    # 简介
    info = db.Column(db.Text)
    # 封面
    logo = db.Column(db.String(255), unique=True)
    # 星级
    star = db.Column(db.SmallInteger)
    # 播放量
    playnum = db.Column(db.BigInteger)
    # 评论量
    commentnum = db.Column(db.BigInteger)
    # 所属标签
    tag_id = db.Column(db.BigInteger, db.ForeignKey('tag.id'))
    # 上映地区
    area = db.Column(db.String(255))
    # 上映时间
    release_time = db.Column(db.Date)
    # 播放时间
    length = db.Column(db.String(100))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # 评论外键关系
    comments = db.relationship('Comment', backref='movie')
    # 收藏外键关系
    moviecols = db.relationship('Moviecol', backref='movie')
    
    def __repr__(self):
        return '<Movie %r>' % self.title


# 上映预告
class Preview(db.Model):
    __tablename__ = 'preview'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 标题
    title = db.Column(db.String(255), unique=True)
    # 封面
    logo = db.Column(db.String(255), unique=True)
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Preview %r>' % self.title


# 评论
class Comment(db.Model):
    __tablename__ = 'comment'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 评论内容
    content = db.Column(db.Text)
    # 所属电影
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    # 所属用户
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Comment %r>' % self.id


# 电影收藏
class Moviecol(db.Model):
    __tablename__ = 'moviecol'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 所属电影
    movie = db.Column(db.Integer, db.ForeignKey('movie.id'))
    # 所属用户
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Moviecol %r>' % self.id


# 权限
class Auth(db.Model):
    __tablename__ = 'auth'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 名称
    name = db.Column(db.String(100), unique=True)
    # 地址
    url = db.Column(db.String(255), unique=True)
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Auth %r>' % self.name


# 角色
class Role(db.Model):
    __tablename__ = 'role'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 名称
    name = db.Column(db.String(100), unique=True)
    # 权限列表
    auths = db.Column(db.String(600), unique=True)
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # 管理员外键关联
    admins = db.relationship('Admin', backref='Role')
    
    def __repr__(self):
        return '<Role %r>' % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = 'admin'
    # 编号
    id = db.Column(db.INTEGER, primary_key=True)
    # 名称
    name = db.Column(db.String(100), unique=True)
    # 密码
    pwd = db.Column(db.String(100))
    # 是否是超级管理员
    is_supper = db.Column(db.SmallInteger)
    # 所属角色
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # 登录日志外键关联
    adminlogs = db.relationship('AdminLog', backref='admin')
    # 操作日志外键关联
    oplogs = db.relationship('OpLog', backref='admin')
    
    def __repr__(self):
        return '<Admin %r>' % self.name


# 管理员登录日志
class AdminLog(db.Model):
    __tablename__ = 'adminlog'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 所属管理员
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 登录IP
    ip = db.Column(db.String(100))
    # 登录时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return '<AdminLog %r>' % self.id


# 管理员操作日志
class OpLog(db.Model):
    __tablename__ = 'oplog'
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 所属管理员
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 操作IP
    ip = db.Column(db.String(100))
    # 操作原因
    reason = db.Column(db.String(600))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return '<OpLog %r>' % self.id


if __name__ == '__main__':
    db.create_all()
