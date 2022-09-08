#5.3 ,5.4
#if,if-else,if-elif-else,利用if语句处理列表
#条件通过某一个测试后就跳过余下测试
age=65
if age<=4:
    print("your admission cost is $0")
elif age<=10 or age>=70:
    print("your admission cost is $5")
elif age<=18 or age>=60:
    print("your admission cost is $10")
else:
    print("your admission cost is $15")

#如果需要对多个可能结果均进行相应操作，则多次使用if，而不能使用elif，else，否则会跳过余下测试步骤

#以下处理列表
requested_toppings = ['mushroom','green peppers','extra cheese']
message1 = "sorry,we are out of this right now!"
message2 = "finished making your pizza!"
for requested_topping in requested_toppings:
    if requested_topping == 'mushroom':
        print(message1.title())
    else:
        print('Adding '+requested_topping+'.')
print('\n'+message2)

#确定列表非空
requested_toppings = []
if requested_toppings:  #进行非空检查
    for requested_topping in requested_toppings:
         print('Adding '+requested_topping+'.')
else:
    print("your choice can't be plain") #对空列表进行反馈

#对多个列表进行操作（核对订单是否有存货）
available_toppings = ['mushroom','olives','green peppers','pepperoni',
                        'pineapple','extra cheese']
requested_toppings = ['mushroom','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding '+requested_topping+'.')
    else:
        print(message1.title())
print(message2.title())

#确定列表非空的情况下确认订单
available_toppings = ['mushroom','olives','green peppers','pepperoni',
                        'pineapple','extra cheese']
requested_toppings = ['mushroom','french fries','extra cheese']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print('Adding '+requested_topping+'.')
        else:
            print('Sorry,We are out of '+requested_topping+' right now!')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want to a plain pizza')