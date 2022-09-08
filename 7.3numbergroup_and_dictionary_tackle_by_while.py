#7.3
#利用while循环处理数组
unconfirmed_users = []  #预分配内存
name = 'a'
while name != 'quit':
    name = input("please enter users'name:")  
    unconfirmed_users.append(name)  #将名字输入待认证名单（数组）
unconfirmed_users.pop()  #忽略去除'quit'
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  #出栈，故顺序与unconfirmed_users顺序相反
    print('verifying user:'+current_user.title())
    confirmed_users.append(current_user)
print('\nAll of the confirmed users:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

while 'alice' in confirmed_users:
    confirmed_users.remove('alice')  #利用while寻找数组中特定元素并删除
print(confirmed_users)

#利用while循环处理字典
#调查问卷的收集
responses = {}  #问卷汇总内存预分配
active = True  #设置一个标志
while active:
    name = input('Please enter your name:')
    prefer = input('Which mountain would you like to climb?')
    responses[name] = prefer  #进行键—值对存储
    #询问是否还有人参加问卷
    repeat  = input("another person's respond?(yes/no)")
    if repeat == 'no':
        active = False

for identity,mountain in responses.items():
    print(identity + "'s favorite mountain is" + ' '+mountain)
