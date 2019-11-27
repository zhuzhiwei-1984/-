from . import 全_蓝图路由, 全_数据库, 类_相册提交表单
from flask import render_template

# 主页_路由 = Blueprint('主页_路由',__name__, static_folder='static', template_folder='templates')
全_相册数据库游标 = 全_数据库['网站数据']['家庭相册']

@全_蓝图路由.route('/相册提交', methods=["GET", "POST"])
def 视图_相册提交():
    # 创建表单对象, 如果是post请求,前端发送了数据,flask会吧数据在构造的表单对象的时候,存放到对象中
    相册提交表单 = 类_相册提交表单()
    # 判断相册提交表单中的数据是否合理
    # 如果表单中的数据完全满足所有的验证器,则返回真
    if 相册提交表单.validate_on_submit():
        # 表示验证合格
        # 提取数据
        局_字符串 = 相册提交表单.字符串.data
        局_文件 = 相册提交表单.文件.data
        局_文件名 = 局_文件.filename
        局_文件.save('python/static/家庭相册/'+局_文件名)
        局_插入数据 = { '路径':'家庭相册/'+局_文件名,
                        '说明': 局_字符串,
                        '类别': 相册提交表单.类别.data
        }
        if not [文件 for 文件 in 全_相册数据库游标.find({'路径':'家庭相册/'+局_文件名})]:
            print('添加一条数据!')
            全_相册数据库游标.insert_one(局_插入数据)
            return render_template('相册提交.html', 表单 = 相册提交表单)
        else:
            print('发现重复数据')
            return render_template('相册提交.html', 表单 = 相册提交表单)

    return render_template('相册提交.html', 表单 = 相册提交表单)
