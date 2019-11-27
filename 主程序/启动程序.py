from flask import Flask, render_template
from app import 全_蓝图路由

全_app = Flask(__name__)
全_app.config['SECRET_KEY'] = '朱志伟爱常文斌'
全_app.register_blueprint(全_蓝图路由)

@全_app.route('/测试')
def 视图_测试():
    return render_template('测试.html')

if __name__ == "__main__":
    print(全_app.url_map)
    全_app.run(port=80,debug=True,host='0.0.0.0')