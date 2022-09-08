#2.3
first_name='ada'
last_name='lovelace'
name=first_name+' '+last_name # "+"为字符串拼接用法

print(name.title())  #所有单词首字母大写
print(name.upper())  #所有字母大写
print(name.lower())  #所有字母小写

message1=name.title()+"\t"+name.upper()+"\n"+name.lower()  #\t tab  \n 换行
print(message1.rstrip())
message2="hello,"+ name.title()+ "!"
print(message2)

language='\tpython\t'
print(language.lstrip()+'!')  #.lstrip()仅仅用于去除字符串 前面 的空格
print(language.rstrip()+'!')  #.rstrip()仅仅用于去除字符串 末尾 的空格
print(language.strip()+'!')   #.strip()用于去除字符串 所有 的空格
print(language+'!')

message="one of python's strength is its diverse community"
print(message) #句子中有单引号时，代表字符串建议使用双引号