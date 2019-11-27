from . import 全_蓝图路由, 全_数据库, session
from flask import render_template, redirect, url_for
import os
import pymongo



全_相册数据库游标 = 全_数据库['网站数据']['家庭相册']
# 主页_路由 = Blueprint('主页_路由',__name__, static_folder='static', template_folder='templates')

@全_蓝图路由.route('/家庭相册')
def 视图_家庭相册():
    数据表 = list()
    数据表 = 全_相册数据库游标.find().sort("_id",-1)
    return render_template('家庭相册.html', 数据表=数据表, )

# @全_蓝图路由.route('/删除相册/<fileID>')
# def 视图_删除相册(fileID):
#     print(fileID)
    
#     路径 = 全_相册数据库游标.find_one({"_id":ObjectId(fileID)})
#     os.rename(os.path.join(os.getcwd(), 'python/static',路径['路径']) ,os.path.join(os.getcwd(), 'python/static/删除相册',路径['路径']))
#     全_相册数据库游标.remove({"_id":ObjectId(fileID)})
#     return redirect(url_for('视图_家庭相册'))

