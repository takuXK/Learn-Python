#3.1   3.2
bicycle=['trek','cannondale','redline','specialized']  #[]表示列表，并用逗号分隔
print(bicycle[0]) #访问列表，注意顺序从0开始
print(bicycle[-1]) #特殊的，索引[-1]永远指向最后一个元素；但是对空列表无效

bicycle[0]='yamaha' #修改列表中元素
print(bicycle[0])

bicycle.append('suzuki')  #append('元素字符')将元素添加到末尾
print(bicycle)

bicycle.insert(2,'honda') #insert(位置编号,'元素字符')添加在列表中的任意位置
print(bicycle)

del bicycle[0] #del删除已知位置索引的元素
print(bicycle)

popped=bicycle.pop(0) #pop弹出列表中指定一个元素，并存储在popped这个变量中，未指定弹出最后一个元素
print(bicycle)

removed='redline'
bicycle.remove(removed) #remove删除列表中一个指定元素，无需知道位置索引
print(bicycle)