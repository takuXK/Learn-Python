#对文件进行切片操作
#log文件是一个分行的文件，文件读取后具有__iter__()方法和__next__()方法，是可迭代对象和迭代器对象
open_file = open('D:\\python\\vs python work\\exercise\\log1')
print(open_file.__iter__())
print(open_file.__next__())
#open_file是无法切片的
try:
    select_file = open_file[100:300]
except:
    print("File can't be sliced!")

#切片的实质：调用了方法__getitem__(slice(start,end,step))，其中slice创建了一个切片实例
numlist = list(range(1,11))
print(numlist.__getitem__(slice(2,8,2)) == numlist[2:8:2])

#1.使用readlines()方法将文件转化为列表再切片
file_list = open_file.readlines()
print(file_list[100:200])
open_file.close()

#2.以上方法过于消耗内存，readlines本质还是读取了文件的全部
#使用itertools.islice返回一个迭代对象切片的生成器
from itertools import islice
open_file = open('D:\\python\\vs python work\\exercise\\log1')
for line in islice(open_file,100,200):
    print(line)
open_file.close()

#3.自己实现islice函数
def My_islice(Iterable,start,end,step=1):
    temp = 0
    for index,element in enumerate(Iterable):
        if index >= end:
            break
        if index >= start:
            if temp == 0:
                temp = step
                yield element
            temp -= 1
print(list(My_islice(numlist,2,8,2))) 
print(list(islice(numlist,2,8,2)))