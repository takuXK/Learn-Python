#去掉字符串中不需要的字符
#过滤用户输入的前后多余的空白字符：
#'    nick2008@gmail.com    '
#过滤Windows下标记文本标识符：
#'hello world\r\n'  \r
#去除文本中Unicode组合符号（例如音调）
#ní hǎo
#1.str.(l/r)strip()  (左/右)两端去除
mail = '    nick2008@gmail.com    '
print(mail.strip())
print(mail.lstrip())
print(mail.rstrip())

#2.切片，然后利用"+"拼接
message = 'hello world\r\n'
print(message[:11] + message[-1])

#3.replace()方法
string = "    abc   edf    "
tackle_string = string.replace(' ','')
print(tackle_string)

#4.使用正则表达式re.sub()
import re
change_string = re.sub('[ \t\n]+','',string)
print(change_string)

#5.translate()方法，需替换值转为Unicode码
string = 'ní hǎo'
deal_string = string.translate({ord('í'):'X'})
print(deal_string)
#应对多种替换场合，利用maketrans()生成映射字典
another_string = 'abcxyz'
fun_ = another_string.maketrans('abcxyz','ABCXYZ')  #生成Unicode对应字典
deal_string = another_string.translate(fun_)  #传入映射字典
print(deal_string)

string = 'ní hǎo'  #í为组合符号长度为2
import unicodedata
#利用unicodedata的combining判断组合符号
#这个方法对于非组合符号返回0，组合符号返回其Unicode值
combined_unicode = [ord(char) for char in string if unicodedata.combining(char)]
trans_dict = dict.fromkeys(combined_unicode,None)
deal_string = string.translate(trans_dict)
print(deal_string)