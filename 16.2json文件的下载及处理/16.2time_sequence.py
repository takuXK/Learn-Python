#16.2.5以后
#时间序列特征
import json
import pygal
import math
from itertools import groupby

#导入数据
filename = r'D:\python\vs python work\16.2json文件的下载及处理\btc_close_2017.json'
with open(filename) as read_file:
    btc_data = json.load(read_file)
dates = []
months = []
weeks = []
weekdays = []
close_prices = []
for btc_index in btc_data:
    dates.append(btc_index['date'])
    months.append(int(btc_index['month']))
    weeks.append(int(btc_index['week']))
    weekdays.append(btc_index['weekday'])
    close_prices.append(int(float(btc_index['close'])))

#利用math包遍历取对数
close_prices_log = [math.log10(_) for _ in close_prices]

#作图
line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title = "收盘价对数变换（￥）"
line_chart.x_labels = dates
N = 20 #每20天显示一次
line_chart._x_labels_major = dates[::N]
line_chart.add('log10(收盘价)',close_prices_log)
line_chart.render_to_file(r'D:\python\vs python work\16.2json文件的下载及处理\收盘价对数变换折线图（￥）.svg')

#求取一定时间的收盘价均值并做图
def draw_line(x_data,y_data,title,y_legend):
    xy_map = []
    #将x,y的数据合并(zip)、排序(sorted)、分组(groupby)
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _: _[0]):
        y_list = [v for _,v in y]
        xy_map.append([x,sum(y_list) / len(y_list)])  #求取平均值
    x_unique,y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

#每月均值
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month],close_prices[:idx_month],'收盘价每月日均值（￥）',
    '每月日均值')
line_chart_month

#每周均值
idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week],close_prices[1:idx_week],'收盘价每周日均值（￥）',
    '每周日均值')
line_chart_week

#按星期均值
idx_weekday = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday', 'Sunday']
#weekday_int存储2017-01-02至2017-12-11各日的星期（数值）
weekday_int = [wd.index(w) + 1 for w in weekdays[1:idx_weekday]]
line_chart_weekday = draw_line(weekday_int,close_prices[1:idx_weekday],"收盘价星期均值（￥）",
    '星期均值')
line_chart_weekday.x_labels = wd
line_chart_weekday.render_to_file('收盘价星期均值（￥）.svg')

#创建数据仪表盘（统合数据）
with open('收盘价Dashboard.html','w',encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><metacharset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图（￥）.svg','收盘价对数变换折线图（￥）.svg','收盘价每月日均值（￥）.svg',
        '收盘价每周日均值（￥）.svg','收盘价星期均值（￥）.svg'
    ]:
        html_file.write('   <object type="image/svg + xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')