#8.6
#外部调用函数：import 模块名
import make
#模块名.函数名(实参)
make.make_car(
    'subaru',
    'outback',
    color = 'blue',
    tow_package = True
)

print('\n')
#还可以导入模块中的特定函数：from 模块名 import 函数名1,函数名2,...
from make import make_car,make_pizza
#使用这种导入形式，在调用函数时无需在加上模块名
make_car('benz','outback',color = 'black',tow_package = False)
make_pizza(12,'mushroom','pepperoni','extra cheese')

#当导入某个模块中的所有函数时，可使用：from 模块名 import *
#由于模块make中只有make_car和make_pizza两个函数，故上述程序等同于：
print('\n')
from make import *
make_car('benz','outback',color = 'black',tow_package = False)
make_pizza(12,'mushroom','pepperoni','extra cheese')

#有时模块名或函数名太长，可使用：模块名 as 简称 或 函数名 as 简称 来缩短调用函数语句
print('\n')
import make as m
m.make_pizza(12,'mushroom','pepperoni','extra cheese')
from make import make_pizza as mp
mp(12,'mushroom','pepperoni','extra cheese')

#注意：实际调用函数前，需要将所有import语句写在文件开头