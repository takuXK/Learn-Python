#10.1从文件中读取数据
#with open(文件名) as 变量名:
#   变量名 = 变量名.read()将文件中的数据存储在变量中
with open('pi_digit.txt') as file_object:
    #打开文件，将文件等效为file_object，使用with将使文件不被访问时关闭
    contents = file_object.read()  #读取
    print(contents.rstrip())  #.rstrip()删除read函数自带的print('\n')

#当文件不在当前目录时，需加入绝对文件路径，开头单引号前加r以原始字符串方式指定路径，防止出错
file_path =r'D:\python\vs python work\10.1读取文件\pi_digit.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#逐行读取(遍历的方法)
with open('pi_digit.txt') as file_object:
    for line in file_object:
        print(line)

#创建包含文件各行内容的列表
with open('pi_digit.txt') as file_object:
    lines = file_object.readlines()  #按行读取存入lines的数组中
    pi_string = ''
    for line in lines:
        pi_string +=line.strip()
    print(pi_string[:17] + '...')  #打印小数点后15位
    print(len(pi_string))

#在圆周率中查找自己的生日
birthday = 0
while birthday != 'quit':
    birthday = input('enter your birthday,in the form mmddyy:')  
    if birthday in pi_string:
        print('found!')
    else:
        print('sorry,not found!')