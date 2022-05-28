#字典值排序
from random import randint
namelist = ['LiLei','Lucy','Rudy','Cathy','Mark','Doublt','Stephen','Henry']
score_dict = {name:randint(60,100) for name in namelist}
print(score_dict)
#1.sorted函数
#字典解析转换为元组列表，且分数在前，使得sorted函有效运作
score_list = [(score,name) for name,score in score_dict.items()]
score_hl = sorted(score_list,reverse=True)
print(score_hl)

#2.使用zip函数转换为元组列表，再使用sorted函数
score_list = list(zip(score_dict.values(),score_dict.keys()))
score_hl = sorted(score_list,reverse=True)
print(score_hl)

#3.直接在sorted函数中设置关键字对字典进行排序
#key参数中传入一个匿名函数，对于每个item组，返回其第二个元素即分数
score_hl = sorted(score_dict.items(),key=lambda x: x[1],reverse=True)
print(score_hl)

#生成标号
for i,(name,score) in enumerate(score_hl,1):  #次序号从1开始
    print(i,name,score)