from flask import Flask, render_template, request, redirect, url_for,session
from jinja2 import Environment, FileSystemLoader
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig
from scratch import queryList, rtdb,read_l
from login_s import login_s
from scratch import send_data

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts_tool import gauge_base_hum,gauge_base_tem,liquid_base_light,line_markpoint,creat_wordcloud

app = Flask(__name__, static_folder="templates")

app.config['SECRET_KEY'] = '3c2d9d261a464e4e8814c5a39aa72f1c'
@app.route("/")
def index():
    if request.method == 'GET':
        if 'uname' in session:
            return render_template("index.html")
        else:
            if 'uname' in request.cookies:
                uname = request.cookies.get('uname')
                session['uname'] = uname
                return render_template("index.html")
            else:
                return redirect('/login')


@app.route("/login",  methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'uname' in session:
            return redirect('/')
        else:
            if 'uname' in request.cookies:
                uname = request.cookies.get('uname')
                session['uname'] = uname
                return redirect('/')
            else:
                return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['passwd']
        rest = login_s(username, password)
        if rest == 'ok':
            resp = redirect('/')
            session['uname'] = username
            if 'isSaved' in request.form:
                # 需要记住密码，将信息保存进cookie
                resp.set_cookie('uname', uname, 60 * 60 * 24 * 30)
            return resp
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

@app.route("/wordcloudChart")
def wordcloudChart():
    c = creat_wordcloud()
    return c.dump_options_with_quotes() 

@app.route("/data", methods=["POST"])
def get_data():
    send_data(request.stream.read())
    return 'ok'

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    resp = redirect('/')
    resp.delete_cookie('uname')
    session.pop('uname', None)
    return resp



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
