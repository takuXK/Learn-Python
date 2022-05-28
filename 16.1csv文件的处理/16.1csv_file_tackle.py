#16.1
#csv文件数据的读取、处理及其可视化
from matplotlib import pyplot as plt
from datetime import datetime
import csv
#分析csv文件头
filename = r'D:\python\vs python work\16.1csv文件的处理\death_valley_2014.csv'
with open(filename) as f_obj:  #存储文件在f_obj中
    reader = csv.reader(f_obj)  #reader方法将创建阅读器对象
    header_row = next(reader)  #next方法返回对应文件的下一行（一次调用即为第一行）
    for index,column_header in enumerate(header_row):
        #enumerate可获取对应数组的索引和值
        print(index,column_header)

    #读取csv中的数据
    dates,highs,lows =[],[],[]  #读取第一列
    for row in reader:
        try:  #保证数据缺失代码也能正常运行
            #方法strptime(读取元素,格式)输入日期
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except:
            print(current_date,'missing data!')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#绘制图表（附带时间）
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)  #alpha指定颜色透明度
plt.plot(dates,lows,c='blue',alpha=0.5)
#fill_between(x,y1,y2)用于填充颜色
plt.fill_between(dates,lows,highs,facecolor='blue',alpha=0.1)
plt.title("Daily high and low temperatures - 2014\nDeath Valley,CA",fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()  #x轴标签分布自适应，避免标签重合
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()