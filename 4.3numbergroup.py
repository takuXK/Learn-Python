#4.3
for value in range(1,6,1):  #对于range(a,b,c)，循环范围是a<=x<b，间隔为c(默认为1)
    print(value)

numbergroup=list(range(1,6))  #list可创建数组
print(numbergroup)

##ex:生成平方数数组
square=[]
for val in range(1,11):
    val=val**2
    square.append(val)
print(square)

#数组解析创建：将简单操作置于for之前
square=[val**2 for val in range(1,11)]
print(square)