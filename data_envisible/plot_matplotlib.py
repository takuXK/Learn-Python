#利用matplotlib作图
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab as plb
#折线图
x = range(1,11)
values1 = [1,5,8,9,2,0,3,10,4,7]
values2 = [3,8,9,2,1,2,4,7,6,6]
#坐标轴设置
ax = plt.axes()  #坐标轴句柄
ax.set_xlim([0,11])
ax.set_ylim([-1,11])
ax.set_xticks(list(range(1,11)))
ax.set_yticks(list(range(0,11)))
ax.grid()
plt.plot(x,values1,'v--',color='b')
plt.plot(x,values2,'o:',color='r')
#字符添加
plt.xlabel('Entries')
plt.ylabel('Values')
plt.annotate(xy=[1,1],text='first entry')
plt.legend(['First','Second'],loc=4)  #loc图例位置在第四象限
plt.show()

#饼图
values = [5,8,9,10,4,7]
colors = ['b','g','r','c','m','y']
labels = []
labels_ord = list(range(65,71))
for i in labels_ord:
    char = chr(i)
    labels.append(char)
explode = (0,0.2,0,0,0,0)
#labels设置标签，explode设置版块的分离，autopct展示版块的百分比
#counterclock决定扇形的方向，shadow决定是否有阴影
plt.pie(values,colors=colors,labels=labels,
        explode=explode,autopct='%1.1f%%',
        counterclock=False,shadow=True)
plt.title('Values')
plt.show()

#柱状图
values = [5,8,9,10,4,7]
widths = [.7,.8,.7,.7,.7,.7]
colors = ['b','g','r','c','m','y']
#align决定柱状图的对齐方式
plt.bar(range(0,6),values,width=widths,color=colors,align='center')
plt.show()

#直方图
x = 20 * np.random.randn(10000)  #生成了一个含有10000个元素且服从正态分布的数组x
#bins为条形数，range为横坐标范围，histtype线条类型，align对齐方式，label图例名称
plt.hist(x,bins=25,range=(-50,50),histtype='step',
    align='mid',color='g',label='Test Data'       
    )
plt.legend()
plt.title('Step Filled Histogram')
plt.show()

#箱线图
spread = 100 * np.random.rand(100)
center = np.ones(50) * 50  #ones(n)生成长度为50，元素全为1的数组
filter_high = 100 * np.random.rand(10) * 100
filter_low = -100 * np.random.rand(10) * 100
data = np.concatenate(
    (spread,center,filter_high,filter_low)
)  #concatenate组合数据
#sym异常点颜色外观，notch=True创建有凹口的箱盒，notch=False为方形箱盒
plt.boxplot(data,sym='gx',widths=0.75,notch=True)
plt.show()

#散点图
x1 = 5 * np.random.rand(40)
x2 = 5 * np.random.rand(40) + 25
x3 = 25 * np.random.rand(20)
x = np.concatenate((x1,x2,x3))
y1 = 5 * np.random.rand(40)
y2 = 5 * np.random.rand(40) + 25
y3 = 25 * np.random.rand(20)
y = np.concatenate((y1,y2,y3))
color_array = ['b'] * 40 + ['g'] * 40 + ['r'] * 20
#s标记点的大小，marker为点的标记
plt.scatter(x,y,s=100,marker='*',c=color_array)
z = np.polyfit(x,y,1)  #polyfit多项式拟合
p = np.poly1d(z)
plb.plot(x,p(x),linestyle='--',color='k')
plt.show()