from . import 全_蓝图路由, 全_数据库, 类_后台登录表单
from flask import render_template, session


全_账户数据库游标 = 全_数据库['网站数据']['账户信息']

# 主页_路由 = Blueprint('主页_路由',__name__, static_folder='static', template_folder='templates')

@全_蓝图路由.route('/后台登录', methods=['GET','POST'])
def 视图_后台登录():
    局_登录表单 = 类_后台登录表单()
    局_状态信息 = '请输入登录信息:'
    if 局_登录表单.validate_on_submit():
        局_账号 = 局_登录表单.账户.data
        局_密码 = 局_登录表单.密码.data
        局_数据核实 = 全_账户数据库游标.find_one({'账号':局_账号})
        if not 局_数据核实:
            局_状态信息 = '账号错误,请重新输入'
        elif 局_数据核实['密码'] != 局_密码:
            局_状态信息 = '密码错误,请重新输入'
        else:
            session['权限'] = '真'
            局_状态信息 = '登录成功!!'
            return render_template('后台登录.html', 提示信息=局_状态信息,状态信息 = session.get('权限','假'))
    return render_template('后台登录.html', 登录表单 = 局_登录表单, 提示信息=局_状态信息,状态信息 = session.get('权限','假'))
