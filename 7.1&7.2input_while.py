#7.1,7.2
#使用input函数来通过外部进行输入
#注意input输入后的变量是str类型，运算需转化
n = input('please enter a number:')
#如果为n = eval(input('please enter a number:'))，那么不用进行类型转化
#eval('字符串')
n = int(n)  #变量类型转化
if n % 10 ==0:
    print('yes!')
else:
    print('no!') 

#while循环
#与for循环针对集合中的所有元素不同，while循环的标准是条件是否符合
#在使用while循环时，要避免无限循环的条件语句
n = 0
while n != 'quit':
    n = input("please enter a number(enter 'quit' to end):")
    n = int(n)
    if n % 10 == 0:
        print(str(n)+' is a multiple of 10')
    else:
        print(str(n)+" isn't a multiple of 10")

#当while有多个要求需满足时，可使用“标志”
active = True  #这里active就是标志，用来控制while是否运行
while active:
    message = input('enter something:')
if message == 'quit':
    active = False
else:
    print(message.title())

#break用于退出while循环
city = []
while True:
    new_city = input('please enter the name of a city you have visited:')
    if new_city == 'quit':
        break
    else:
        city.append(new_city)
print(city)

#continue使得程序返回while循环开头
n = 0
while n <= 10:
    n += 1  #n=n+1
    if n % 2 ==0:
        continue
    print(n)  #只输出奇数1,3,5,7,9,11