#实现对象的反向迭代
#常规反向迭代方法
#1.reverse()方法先将列表反序
num_list = [1,2,3,4,5]
num_list.reverse()
for i in num_list:
    print(i)
#2.以上方法改变量源列表，使用切片方法可以避免
num_list = [1,2,3,4,5]
print(num_list[::-1])
#3.使用reversed生成反向迭代器，reversed和iter相反
#同样有__reversed__方法
rever_list = reversed(num_list)
print(rever_list)

#实现一个连续浮点数发生器FloatRange，根据给定范围和步进值产生可正向迭代也可反向迭代的序列
class FloatRange():
    def __init__(self,start,end,step):
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):  #正向迭代方法
        num = self.start
        while num <= self.end:
            yield num
            num += self.step
    def __reversed__(self):  #反向迭代方法
        num = self.end
        while num >= self.start:
            yield num
            num -= self.step

fr = FloatRange(3.0,4.0,0.2)
for num in fr.__iter__():
    print(num)
print('-' * 20)
for num in fr.__reversed__():
    print(num)

#以上迭代过程中存在浮点数精度运算问题，使用decimal可解决
from decimal import Decimal
from functools import reduce

print(reduce(Decimal.__add__,[Decimal('0.2')] * 5))
print(reduce(Decimal.__add__,[Decimal(0.2)] * 5))

class FloatRangex():
    def __init__(self,start,end,step):
        self.start = Decimal(str(start))
        self.end = Decimal(str(end))
        self.step = Decimal(str(step))
    def __iter__(self):  #正向迭代方法
        num = self.start
        while num <= self.end:
            yield float(num)
            num += self.step
    def __reversed__(self):  #反向迭代方法
        num = self.end
        while num >= self.start:
            yield float(num)
            num -= self.step

print('\n')
fr = FloatRangex(3.0,4.0,0.2)
for num in fr.__iter__():
    print(num)
print('-' * 20)
for num in fr.__reversed__():
    print(num)