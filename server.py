import time

from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig
from scratch import queryList, rtdb
from login_s import login_s

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Gauge, Line, Liquid

app = Flask(__name__, static_folder="templates")


def gauge_base_tem() -> Gauge:
    s = rtdb()[0]
    c = (
        Gauge(init_opts=opts.InitOpts(width="400px", height="400px"))
            .add('',
                 min_=-20,
                 max_=60,
                 split_number=8,
                 data_pair=[('实时温度\n\n', s)],
                 axisline_opts=opts.AxisLineOpts(
                     linestyle_opts=opts.LineStyleOpts(
                         color=[(0.1875, '#3742fa'), (0.4375, '#1e90ff'), (0.625, '#2ed573'), (0.75, '#d35400'),
                                (1, '#c0392b')], width=25
                     )
                 )
                 )
            .set_global_opts(title_opts=opts.TitleOpts(title="实时温度", pos_left='center'))
    )
    return c


def gauge_base_hum() -> Gauge:
    s = rtdb()[1]
    c = (
        Gauge(init_opts=opts.InitOpts(width="400px", height="400px"))
            .add('',
                 data_pair=[('实时湿度\n\n', s)],
                 axisline_opts=opts.AxisLineOpts(
                     linestyle_opts=opts.LineStyleOpts(
                         color=[(0.45, '#1e90ff'), (0.75, '#2ed573'),
                                (1, '#c0392b')], width=25
                     )
                 )
                 )
            .set_global_opts(title_opts=opts.TitleOpts(title="实时湿度", pos_left='center'))
    )
    return c


def line_markpoint() -> Line:
    hour = int(time.strftime('%H', time.localtime(time.time())))
    l1 = [str(i) for i in range(hour, -1, -1)]
    l2 = [str(i) for i in range(23, hour, -1)]
    s = queryList()
    print(s[0], s[1])
    c = (
        Line()
            .add_xaxis(xaxis_data=l1 + l2)
            .add_yaxis('tem',
                       s[0],
                       )
            .add_yaxis('hum',
                       s[1],
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title="过去24小时温湿度变化曲线"))

    )
    return c


def liquid_base_light() -> Liquid:
    x = 0.54
    c = (
        Liquid()
            .add(
            "test",
            [0.68],
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode('{}%'.format(x * 100)
                                 ),
                position="inside",
            ),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="光照强度"))
    )
    return c


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


@app.route("/data", methods=["POST"])
def get_data():
    print(request.stream.read())
    return 'hello'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
