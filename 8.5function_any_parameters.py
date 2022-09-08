#8.5
#有时一个函数调用时接收的实参数量是不固定的
#形参名*toppings中的*创建了一个名为toppings的空元组()，并将接收的所有实参存入该元组
def make_pizza(size ,*toppings):
    #如果函数中有单接收参数和未知接收量参数，需在函数定义时将接收任意数量的参数放在最后
    print("You have ordered a " + str(size) + "-inch pizza!")
    for topping in toppings:
        print("You have ordered adding " + topping + '!')
make_pizza(16,'pepperoni','cheese','mushroom')

#函数调用时需要接受未知数量且位置类型的实参，这时可将函数编写成能接受任意数量的键-值对
#**user_info创建了一个名为user_info的空字典{}，并将接受的所有的键—值对存入该字典
def build_profile(first_name,last_name,**user_info):
    profile = {}
    profile['first name'] = first_name
    profile['last name'] = last_name
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',location='princeton',field='physics')
#注意输入**user_info时格式为：key = 'value'
print(user_profile)

