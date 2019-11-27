from . import 全_蓝图路由
from flask import render_template

# 主页_路由 = Blueprint('主页_路由',__name__, static_folder='static', template_folder='templates')

@全_蓝图路由.route('/家庭影院')
def 视图_家庭影院():
    return render_template('家庭影院.html')
    # return "大家好"
