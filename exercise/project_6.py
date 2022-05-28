#记录程序的历史记录功能
#双端队列deque（两侧都可出栈入栈的队列）
from collections import deque
seq = deque([],5)
seq.append(1)  #右端入队
seq.appendleft(2)  #左端入队
seq.appendleft(3)
print(list(seq))
seq.pop()  #右端出队
seq.popleft()  #左端出队
print(list(seq))

#利用deque记录猜数小程序运行过程中输入的数字，输入history查看
from random import randint
import pickle  #历史记录的存储

def guess(real_num,guess_num):
    if real_num > guess_num:
        print("猜小了\n")
        return True
    elif real_num < guess_num:
        print("猜大了\n")
        return True
    else:
        print("正确\n")
        return False

def main():
    real_num = randint(0,100)
    flag = 1
    history = deque([],100)
    while flag:
        guess_num = input("请输入一个0至100的整数(输入q离开，输入history查看历史记录)：")
        if guess_num == 'q':
            flag = 0
        elif guess_num == 'history':
            for _ in range(len(history)):
                element = history.popleft()  #顺序出栈
                print(str(element))
        elif not guess_num.isdigit():
            print("无效输入\n")
        elif int(guess_num) > 100 or int(guess_num) < 0:
            print('无效输入\n')
        else:
            history.append(int(guess_num))
            flag = guess(real_num,int(guess_num))
        if flag == False:
            filename = 'D:\\python\\vs python work\\exercise\\history_data.pkl'
            file_obj = open(filename,'wb')  #.pkl需写二进制文件
            pickle.dump(history,file_obj)  #保存历史记录，以备使用

main()

#导回历史记录
filename = 'D:\\python\\vs python work\\exercise\\history_data.pkl'
file_obj = open(filename,'rb')
file_content = pickle.load(file_obj)
print(list(file_content))