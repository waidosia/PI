import time

from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig
from pyecharts import options as opts
from pyecharts.charts import Gauge, Line, Liquid, WordCloud
from scratch import queryList, rtdb
def gauge_base_tem() -> Gauge:
    """
    实现温度指针
    """
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
    """
    实现湿度指针
    """
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
    # hour = int(time.strftime('%H', time.localtime(time.time())))
    hour = int(time.strftime('%H', time.localtime(1639234714)))
    l =  [str(i) for i in range(hour, -1, -1)] + [str(i) for i in range(23, hour, -1)]
    s = queryList()
    print(s[0], s[1])
    c = (
        Line()
            .add_xaxis(xaxis_data=l)
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


# 词条
data = [
    ("智能家居", "1500"),
    ("编程", "777"),
    ("python", "500"),
    ("Flask", "555"),
    ("温度", "100"),
    ("湿度", "100"),
    ("控制", "80"),
    ("pyecharts", "99"),
    ("arduino", "50"),
    ("html", "60"),
    ("css", "20"),
    ("js", "70"),
    ("Mqtt", "120"),
   
]
# 创建词云
def creat_wordcloud() -> WordCloud:
    c = (
    WordCloud()
    .add(series_name="所用技术", data_pair=data, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="所用技术", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    )
    return c 