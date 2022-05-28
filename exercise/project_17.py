#在一个for循环中迭代多个可迭代对象（并行迭代和串行迭代）
from random import randint
#并行：某班期末考试成绩语数英分别存储在3个列表中，同时迭代3个列表，计算每人的总分
#创建班级各科目成绩列表
chinese = [randint(60,100) for _ in range(20)]
math = [randint(60,100) for _ in range(20)]
english = [randint(60,100) for _ in range(20)]
#使用函数zip()合并列表
#zip将各列表对应位置各元素生成一个元组再合并元组，若存在不等长列表情况，则以最短列表为准，后面位置不生成
print(list(zip([1,2,3],[4,5,6],[7,8])))
total_score = []
for score_tuple in zip(chinese,math,english):
    total_score.append(sum(score_tuple))
print(total_score)
#上述方法的列表解析
total_score = [sum(score_tuple) for score_tuple in zip(chinese,math,english)]
print(total_score)
#使用map函数
total_score = list(map(sum,zip(chinese,math,english)))
print(total_score)
#map自身也支持并行迭代
total_score = list(map(lambda c_score,m_score,e_score: c_score + m_score + e_score,chinese,math,english))
print(total_score)

#串行：4个班的英语成绩分别存储在4个列表当中，依次迭代4个列表统计成绩高于90的人数
#利用itertools.chain()将多个可迭代对象进行连接
from itertools import chain
for x in chain([1,2,3],[4,5,6,7],[8,9]):
    print(x)
#创建各班级某科目成绩列表
class1 = [randint(60,100) for _ in range(20)]
class2 = [randint(60,100) for _ in range(21)]
class3 = [randint(60,100) for _ in range(23)]
class4 = [randint(60,100) for _ in range(25)]
list90 = [everyone for everyone in chain(class1,class2,class3,class4) if everyone >= 90]
count = len(list90)
print(str(count) + '人')