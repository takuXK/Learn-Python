#列表中多个字符串的拼贴
char_list = ["<0112>","<32>","<1024x768>","<60>","<1>","<100.0>","<500.0>"]

import datetime  #计算运行时间

#1.使用字符串 + 运算
start_time = datetime.datetime.now()
string = ''
for char in char_list:
    string += char
print(string)
end_time = datetime.datetime.now()
print("方法1运行时间：" + str(end_time-start_time))

#2.使用str.__add__方法（类），结合reduce函数
#事实上，字符串的 + 运算建立在该方法基础上
from functools import reduce
start_time = datetime.datetime.now()
string = reduce(str.__add__,char_list)
print(string)
end_time = datetime.datetime.now()
print("方法2运行时间：" + str(end_time-start_time))

#以上方法比较占用内存，加长运行时间
#3.使用str.join()方法，他是一次完成的
start_time = datetime.datetime.now()
string = ''.join(char_list)
print(string)
end_time = datetime.datetime.now()
print("方法3运行时间：" + str(end_time-start_time))