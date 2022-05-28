#为元组中每个元素命名
student = ('Jim',16,'male','jim8721@gmail.com')
teacher = (30,'Bach','bach6213@foxmail.com','female')
#1.元组数据结构顺序固定，定义数值常量（类似C的#define）
NAME,AGE,SEX,EMAIL = range(4)
def fun(student):
    if student[AGE] < 18:
        pass
    if student[SEX] == 'male':
        pass
    #........

fun(student)

#2.顺序结构不固定，使用枚举类型更方便
from enum import IntEnum
class StudentNum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3

class TeacherNum(IntEnum):
    AGE,NAME,EMAIL,SEX = range(4)

print(student[StudentNum.NAME])
print(teacher[TeacherNum.AGE])

#2.使用标准库collections.namedtuple对元组进行命名
from collections import namedtuple
student = namedtuple('Student',['NAME','AGE','SEX','EMAIL'])  #创建一个类
st = student('Jim',SEX='male',AGE=16,EMAIL='jim8721@gmail.com')  #根据上面的类创建实例
print(isinstance(st,tuple))  #类返回类型为元组
print(st[AGE])
