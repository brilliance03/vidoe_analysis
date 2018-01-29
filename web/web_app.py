# -*- coding:utf-8 -*-
# progammer = 'lizheng'

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app_name = '视频分析系统管理配置端'
app = Flask(app_name)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('test.html', app_name=app_name)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('inputUsername', type=str)
    password = request.form.get('inputPassword', type=str)

    print('username is %s, password is %s' % (username, password))

    return 'welcome, %s, your password is %s' % (username, password)

if __name__ == '__main__':
    app.run()


