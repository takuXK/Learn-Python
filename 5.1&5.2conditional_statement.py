#5.1  5.2 

#条件测试(布尔表达式)：使用 and 和 or 来检查多个条件

#检查特定值是否 包含 在列表中：（使用in）
request_toppings=['mushrooms','onions','pineapple']
a='mushrooms' in request_toppings
b='pepper' in request_toppings
print(a)
print(b)

#检查特定值是否 不包含 在列表中：（使用not in）
a='mushrooms' not in request_toppings
b='pepper' not in request_toppings
print(a)
print(b)