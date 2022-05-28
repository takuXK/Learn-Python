#字符串对齐格式
load_dict = {
    "lodDist":100.0,
    "SmallCull":0.04,
    "DistCull":500.0,
    "trilinear":40,
    "farclip":477
}
width = max(map(len,load_dict.keys()))  #确定输出长度
#1.str.ljust(长度,填充字符),str.rjust(长度,填充字符),str.center(长度,填充字符)方法
for name,value in load_dict.items():
    print(name.ljust(width),':',value)  #右对齐，居中同理

#2.format函数（方法），调用类__format__()方法
for name,value in load_dict.items():
    print(format(name,'<'+str(width)),':',value)

string = 'abcdefg'
#{:填充字符/对齐格式/长度}.format()
print("{:+^20}".format(string))
print(string.__format__('+<20'))

#对于数字，format(数字,'+')表示总输出符号
print(123,'+')
print(-123,'+')
#数字对齐方法，保持数字位数
print(format(123,'0=+10'))
print(format(-123,'0=+10'))