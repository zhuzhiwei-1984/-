from . import 全_蓝图路由
from flask import render_template, session

# 主页_路由 = Blueprint('主页_路由',__name__, static_folder='static', template_folder='templates')

@全_蓝图路由.route('/')
def 视图_主页():
    return render_template('主页.html',状态信息 = session.get('权限','假'))
    # return "大家好"
