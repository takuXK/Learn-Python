#10.2
#写入文件
#with open(文件名,'w') as 变量名:
#   变量名.write(内容)
filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")  #注意python只能将字符串写入文件
    file_object.write("I love creating new games.\n")

#在文件中附加内容
#with open(文件名,'a') as 变量名:
#   变量名.write(内容)
with open(filename,'a') as file_add:
    file_add.write('I also love finding meanings in large datasets.\n')
    file_add.write("I love creating apps that can run in browser.\n")