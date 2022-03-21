import time

from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig
from scratch import queryList, rtdb
from login_s import login_s

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts_tool import gauge_base_hum,gauge_base_tem,liquid_base_light,line_markpoint,creat_wordcloud

app = Flask(__name__, static_folder="templates")


@app.route("/")
def index():
    return render_template("login.html", text='请登录')


@app.route("/show")
def show():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form['uname']
    password = request.form['passwd']
    rest = login_s(username, password)
    if rest == 'ok':
        return redirect(url_for('show'))
    else:
        return render_template("login.html", text='账号密码错误')


@app.route("/tem")
def get_tem():
    c = gauge_base_tem()
    return c.dump_options_with_quotes()


@app.route("/hum")
def get_hum():
    c = gauge_base_hum()
    return c.dump_options_with_quotes()


@app.route("/line")
def get_line():
    c = line_markpoint()
    return c.dump_options_with_quotes()


@app.route("/light")
def get_light():

    c = liquid_base_light()
    return c.dump_options_with_quotes()

@app.round("/wordcloudChart")
def wordcloudChart():
    c = creat_wordcloud()
    return c.dump_options_with_quotes()
s

@app.route("/data", methods=["POST"])
def get_data():
    print(request.stream.read())
    return 'hello'




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
