#在列表、字典、集合中筛选特定数据
#列表解析、filter函数、字典解析、集合解析
#解析：[{(数据格式 for 数据 in 变量名 if 数据所需满足的条件)}]
from random import randint
#迭代体变量_，不使用i是因为没用到变量i
data = [randint(-10,10) for _ in range(10)]
print(data)
#列表解析
res1 = [x for x in data if x >= 0]
print(res1)
#filter函数：filter(lambda函数,需处理列表)
res2 = filter(lambda x: x >= 0,data)
print(list(res2))

#字典解析
new_dict = {'student%d' % _:randint(50,100) for _ in range(1,21)}
for key,value in new_dict.items():
    print(key +':' + str(value))
res3 = {key:value for key,value in new_dict.items() if value>=90}
print('\n')
for key,value in res3.items():
    print(key + ':' + str(value))
#filter函数
res4 = filter(lambda item: item[1] >= 90,new_dict.items())
print('\n')
for key,value in dict(res4).items():
    print(key +':' + str(value))

#集合解析
tup = {randint(0,20) for _ in range(20)}
print(tup)
res5 = {x for x in tup if x % 3 == 0}
print(res5)
#filter函数
res6 = filter(lambda x: x%3==0,tup)
print(set(res6))