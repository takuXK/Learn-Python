#9.5标准库
#python有一个标准库可以直接导入特定的类
from collections import OrderedDict
#OrderedDict类创建字典并记录输入顺序
favorite_language = OrderedDict()  #利用OrderedDict创建实例——一个记录输入顺序的空字典
favorite_language['jen'] = 'python'
favorite_language['sarah'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'
for name,language in favorite_language.items():
    print(name.title() + " likes " +language.title())

from random import randint  #random库
class Die():
    #创建一个具有sides面的骰子
    def __init__(self,sides=6):
        self.sides = sides
    def roll_die(self):
        x = randint(1,self.sides)
        return x

dice = Die(10)
for n in range(0,10):
    y = dice.roll_die()
    print(str(y))