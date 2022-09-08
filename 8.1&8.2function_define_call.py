#8.1,8.2
#定义函数:def 函数名(形参名（括号内空着即无输入变量）):
def greet_users(name):
    print('Hello,' + name.title() + '!')
greet_users('eric')  #调用函数，这里的'eric'为函数调用中的实参

#当一个函数有多个参数时，尝试以下几种方式
#1.位置实参，即实参按形参顺序调用
def animal_describe(type,name):
    print("I have a " + type + " called " + name)
animals = {
    'dog':'a',
    'cat':'b',
    'bird':'c',
    'turtle':'d'
}
for animal_type,animal_name in animals.items():
    animal_describe(animal_type,animal_name)
#2.关键字实参，将调用的形参各自对应赋值，只要将各参数对应上，即使实参顺序与函数形参不一致也不会出错
for animal_type,animal_name in animals.items():
    animal_describe(name=animal_name,type=animal_type)
    #上语句等同于:
    #animal_describe(animal_type,animal_name)
    #animal_describe(type = animal_type,name = animal_name)

#当一个函数的其中几个参数是默认值时，可直接在函数中标定
def pet_describe(name, type='dog'):  #注意应将含默认值的参量写在后面，不允许非默认参数跟随默认参数
    print("I have a " + type + ' called ' + name)
for animal_name in animals.values():
    pet_describe(name=animal_name)
#即使在函数定义中使用了默认参数，当该默认参数有实参输入时，默认参数将被忽略
pet_describe('willie','cat')

#以上函数调用可混合使用