#4.1   4.2
magicians=['alice','david','carolina']
for magician in magicians:  #for循环：依次从列表magicians中取出一个元素存储在magician中
    print(magician.title()) #注意循环后每次print指令都自带换行符\n
    print("a good magician!")
    print(magician.title()+",a good magician!")
print("all of them plays a magic trick!")