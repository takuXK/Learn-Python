#15.2
#绘制简单的折线图matplotlib
import matplotlib.pyplot as plt  #导入pyplot模块
import os
x = range(1,6)
squares = [1,4,9,16,25] #y值，x值默认[1,2,3,4,5]
plt.plot(x,squares)  #plot作图
plt.show()  #打开matplotlib查看器，显示图形
plt.close()

#修改线条粗细
plt.plot(x,squares,linewidth=5)
#加入图形标题和坐标轴标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记大小
plt.tick_params(axis='both',labelsize=14)  #'both'指定实参将同时影响x,y轴
plt.show()
plt.close()

#绘制散点图
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]  #相当于一句for循环遍历了x_values计算其平方值
#设置属性：c点的颜色，cmap颜色映射，edgecolors点轮廓是否存在，s点的大小
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize =14)
plt.tick_params(axis='both',labelsize=14)
#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.show()
#保存图表：将plt.show()替换为以下语句
#os.chdir('D:\\python\\vs python work\\15.2简单图像')
#plt.savefig('squares_plot.png',bbox_inches='tight')  #第二个参数表示将图像多余空白部分除去