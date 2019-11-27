from . import 全_蓝图路由
from flask import render_template

# 主页_路由 = Blueprint('主页_路由',__name__, static_folder='static', template_folder='templates')

@全_蓝图路由.route('/关于我们')
def 视图_关于我们():
    return render_template('关于我们.html')
    # return "大家好"
