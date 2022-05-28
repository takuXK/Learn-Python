#16.2.5以前
#json文件数据的读取、处理
from matplotlib import pyplot as plt
from datetime import datetime
import pygal
import json
#json文件的读取
filename = r'D:\python\vs python work\16.2json文件的下载及处理\btc_close_2017.json'
with open(filename) as f_obj:
    btc_data = json.load(f_obj)
for group in btc_data:
    date = group['date']
    month = int(group['month'])
    week = int(group['week'])
    weekday = group['weekday']
    close_price = int(float(group['close']))  #int()无法直接将浮点数转化为数字格式
    print("{} is month {} week {},{},the close price is ￥{}".format(date,month,week,weekday,close_price))

#绘制股票走势折线图(利用matplotlib)
dates,months,weeks,weekdays,close = [],[],[],[],[]
for btc_dict in btc_data:
    cd = datetime.strptime(btc_dict['date'],"%Y-%m-%d")
    dates.append(cd)
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,close,c='red',alpha=0.8)
plt.title("Daily price")
plt.xlabel('date',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("price(RMB)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
plt.close()

#绘制股票走势折线图(利用pygal)
dates,months,weeks,weekdays,close = [],[],[],[],[]
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
#利用pygal创建Line实例，x_label_rotation让x轴上的标签旋转20°，
#show_minor_x_labels=False则告诉程序无需显示全部的x轴标签
line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart._title = "收盘价（￥）"
line_chart._x_labels =  dates
N = 20  #每隔20天显示一次x轴标签
line_chart._x_labels_major = dates[::N]
line_chart.add('收盘价',close)  #添加图例
#保存矢量图
line_chart.render_to_file(r'D:\python\vs python work\16.2json文件的下载及处理\收盘价折线图（￥）.svg')