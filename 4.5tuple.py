#4.5 
dimensions=(200,50)  #元组：元组中的元素不可修改，即不可变列表；使用()
print(dimensions)
print(dimensions[0])  #可索引
for dimension in dimensions:  #可遍历
    print(dimension)

dimensions=(100,400)  #但是存储元组的变量可以赋值为其他不同的元组
print(dimensions)