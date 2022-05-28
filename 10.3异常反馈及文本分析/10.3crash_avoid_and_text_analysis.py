#10.3
#有些代码并未导致error但是也会输出traceback，应该尽量避免
print("Give me two numbers and I'll divide them")
print("Enter 'q' to quit")
while True:
    first_number = input('first number:')
    if first_number == 'q':
        break
    second_number = input('second number:')
    try:
        #尝试可能出错的代码块
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:  #except 错误类名
        #出错后的响应
        print("You can't divide by 0!")
    else:
        print(answer)

#split()函数以空格为界创建一个列表包含所有的字符串
#利用该函数可以统计字数
def count_words(filename):
    try:
        with open(filename) as f_obj:
            article = f_obj.read()
    except FileNotFoundError:
        print("Sorry,we didn't find " + filename + '.')
        #若在except发生时想让程序什么都不做，使用pass
    else:
        article_g = article.split()
        num = len(article_g)
        print("There're " + str(num) + " words in " + filename)
filenames = ['introduction1.txt','introduction2.txt','introduction3.txt']
for filename in filenames:
    count_words(filename)