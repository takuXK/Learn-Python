#8.3
#函数可以指定返回值，使用return 变量名，这时调用函数时前面可加变量名来接受函数的输出
def full_name_combine(first_name,last_name,middle_name=''):
    #在定义函数时可以通过给选择性输入的参数赋一个默认值来将该参数变为选择性输入参数
    if middle_name:  #认为非空字符为True
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    
    return full_name.title()

full_name1 = full_name_combine('jimi','hendrix')
full_name2 = full_name_combine('john','hooker','lee')
print(full_name1 + '\n' + full_name2)

#利用函数创建字典
def build_person(first_name,last_name,age=''):
    person = {'first name':first_name,'last name':last_name}
    if age:
        person['age'] = age
    return person
personlist = {}
while True:
    first = input('Please enter a first name:')
    print("Enter 'quit' to quit")
    if first =='quit':
        break
    last = input('Please enter a last name:')
    print("Enter 'quit' to quit")
    if last == 'quit':
        break
    age = input('please enter an age:')
    print("Enter 'quit' to quit")
    if age == 'quit':
        break
    personlist = build_person(first,last,age)
    print('Hello,' + personlist['first name'] + ' ' + personlist['last name'])