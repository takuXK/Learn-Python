#6.1,6.2
#"字典"(items)是一系列 键—值对，使用{}表示，能存储不同类型的信息（值），不同类型的信息类别（键）名称后需加":"
#"字典"的格式：变量名 = {类型名1:名称1,名称2,...,类型名2:名称1,名称2,...}

#创建字典,调用字典
alien_0 = {'color': 'green','points': 5}
print(alien_0['color']) #变量名[类型名]调用信息（值）
new_points = alien_0['points']
print('you just earned '+str(new_points)+' points!')
#在字典中添加键—值对
alien_0['x_position'] = 0  #变量名[首次出现的类型名] = ...
alien_0['y_position'] = 25
print(alien_0)
#修改字典中的键—值对
alien_0['color'] = 'yellow'  #变量名[已有的类型名] = ...
print(alien_0)
#删除字典中的键—值对
del alien_0['points']  #del 变量名[已有的类型名]
print(alien_0)