#快速寻找多个字典中的公共键（每轮进球情况匹配）
from random import randint,sample  #随机取样
goal_members = sample('abcdefg',randint(3,6))  #选取进球成员
#创建各轮球员进球情况字典
goal_dict1 = {goal_member:randint(1,4) for goal_member in goal_members}
goal_dict2 = {goal_member:randint(1,4) for goal_member in goal_members}
goal_dict3 = {goal_member:randint(1,4) for goal_member in goal_members}
#1.逐一匹配（已知轮数）
common_goal_members = [goal_member for goal_member in goal_dict1 if goal_member in goal_dict2 and goal_member in goal_dict3]
print(common_goal_members)
#2.使用map(函数,序列)函数判断各球员是否在所有字典当中
goal_dict = [goal_dict1,goal_dict2,goal_dict3]
common_goal_members = [goal_member for goal_member in goal_dict[0] if all(map(lambda goal_dict: goal_member in goal_dict,goal_dict[1:]))]
print(common_goal_members)
#3.集合的交集&
from functools import reduce
#reduce函数将自身输入函数的返回值一直与另外新输入的变量进行输入函数的操作
goal_members_dict = map(dict.keys,[goal_dict1,goal_dict2,goal_dict3])  #获取所有球员
common_goal_members = reduce(lambda dict1,dict2: dict1&dict2,goal_members_dict)
print(common_goal_members)