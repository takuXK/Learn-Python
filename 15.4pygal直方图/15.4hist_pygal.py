#15.4
#利用pygal绘制直方图
from random import randint
import unittest
import pygal
import os
#创建骰子类
class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        result = randint(1,self.num_sides)
        return result

#多次投掷骰子并检验正确性
class TestDie(unittest.TestCase):
    def testdiecorrection(self):
        die = Die()
        N = 101  #投掷N-1次
        n = 1  #计数
        results = []
        while n < N:
            result = die.roll()
            results.append(result)
            n += 1
        for result in results:
            self.assertTrue(result > 0 and result < 7)
unittest.main()

#数据统计(以下程序请删除上述检测代码运行)
die = Die()
results = []
N = 1000  #投掷N次
for roll_num in range(N):
    result = die.roll()
    results.append(result)
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)  #数组名.count(特定值) 可对特定值计数
    frequencies.append(frequency)
print(frequencies)

#利用pygal绘制直方图
hist = pygal.Bar()  #创建Bar实例hist
hist.title = "Result of rolling one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']  #x轴标签
hist._x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add('D6',frequencies)  #add()将一系列值添加到图表中
os.chdir('D:\\python\\vs python work\\15.4pygal直方图')
hist.render_to_file('die_visual.svg')