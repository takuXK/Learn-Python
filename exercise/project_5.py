#让字典有序
from random import randint,shuffle
#1.使用标准库collections的OrderedDict
names = list('abcdefg')
shuffle(names)  #打乱名字，以便产生名次
from collections import OrderedDict
order_dict = OrderedDict()  #创建一个空字典，这个字典会自动排序
for rank,name in enumerate(names,1):  #编号
    order_dict[name] = rank
print(order_dict)
#根据名字查询名次
def Query_By_Name(order_dict,name):
    return order_dict[name]

query_name = 'e'
rank = Query_By_Name(order_dict,query_name)
print(query_name + "'s rank is " + str(rank))
#根据名次（名次范围）查询名字
#OrderedDict不支持直接切片，而应使用islice
from itertools import islice
#islice(切片对象序列,切片起始索引（包括）,切片末索引（不包括）)通过迭代来切片
def Query_By_Order(order_dict,init,end=None):  #无参数end，查询单个名次；有则查询名次范围
    namelist = islice(order_dict,init-1,end)
    return list(namelist)

init,end = 1,5
namelist = Query_By_Order(order_dict,init,end)
print("Rank " + str(init) + " to " + str(end) + ":" + '\n') 
for name in namelist:
    print(name)