#10.4
#使用json格式存储数据：json.dump(存储内容,存储文件名)
import json
n = [2,3,5,7,11,13]
filename = 'numbers.json'
with open(filename,'w') as f_obj:  #先打开文件
    json.dump(n,f_obj)

#读取json文件：json.load(存储文件名)
with open(filename) as f_obj:
    p = json.load(f_obj)
    print(p)

#获取用户名，区分系统以存储的用户名和新用户名
import json
def get_stored_username(filename):
    #检查是否为已存储用户名
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    #存储新用户名
    username = input("What's your name?")
    filename = username + '.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username
def greet_user(filename):
    #基于新旧用户的判断作出决策
    username = get_stored_username(filename)
    if username:
        print("Welcome back," + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back," + username + '!')

greet_user('eric.json')