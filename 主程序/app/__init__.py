from flask import Blueprint, session
from flask_wtf import FlaskForm
from wtforms import StringField,FileField, SubmitField, BooleanField,SelectMultipleField, PasswordField
from wtforms.validators import DataRequired, AnyOf
from flask_wtf.file import FileField as File, FileRequired, FileAllowed
from bson import ObjectId
import pymongo
全_数据库 = pymongo.MongoClient('192.168.31.220')

class 类_相册提交表单(FlaskForm):
    '''相册提交表单类'''
    字符串 = StringField(label='请输入图像介绍', validators=[DataRequired('数据不能为空')])
    文件 = FileField(label='请选择上传的图片', validators=[FileRequired('数据不能为空'), FileAllowed(['jpg','jpeg','png','gif'])])
    类别 = SelectMultipleField(label='请选择类型',choices=[('小主子','小主子'), ('小朱子','小朱子'),('小兔子','小兔子'),('其他','其他')])
    提交按钮 = SubmitField('提交')

class 类_后台登录表单(FlaskForm):
    '''后台登录表单模块'''
    账户 = StringField(label='请输入用户名', validators=[DataRequired('用户名不能为空')])
    密码 = PasswordField(label='请输入密码', validators=[DataRequired('密码不能为空')])
    登录按钮 = SubmitField('提交')

全_蓝图路由 = Blueprint('全_蓝图路由', __name__)

from .视图_主页 import 视图_主页
from .视图_家庭相册 import 视图_家庭相册
from .视图_家庭书屋 import 视图_家庭书屋
from .视图_家庭影院 import 视图_家庭影院
from .视图_后台登录 import 视图_后台登录
from .视图_相册提交 import 视图_相册提交
from .视图_关于我们 import 视图_关于我们
