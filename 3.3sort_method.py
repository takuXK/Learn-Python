cars=['bmw','audi','toyota','subaru']
cars1=sorted(cars)  #sorted是一个将列表 临时 按字母正序排序的函数
cars2=sorted(cars,reverse=True)  #传递参数reverse=True可令列表 临时 按字母反序排序
print("sorted list:"+ str(cars1))
print("reverse sorted list:"+ str(cars2))
print('origin list:'+ str(cars))

cars=['bmw','audi','toyota','subaru']
cars.sort()  #.sort将列表 永久 按字母正序排序
print(cars)
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)  #传递参数reverse=True可令列表 永久 按字母反序排序
print(cars)

cars=['bmw','audi','toyota','subaru']
cars.reverse()  #reverse是将当前列表 永久 倒序排序
print(cars)

num=len(cars)  #len是一个获取列表长度的函数
print(num)