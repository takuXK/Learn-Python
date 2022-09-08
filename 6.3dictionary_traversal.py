#6.3
#字典的遍历
#1.遍历所有的键—值对
#for 变量名1,变量名2 in 字典变量名.items():
#变量名1存储键，变量名2存储值
favorate_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}  #当一个键对应多个值时，将所有值用[]包括
for key,value in favorate_languages.items():
    print("\nname:" + key.title())
    print("favorate language:" + value.title())

#2.遍历所有的键
#for 变量名 in 字典变量名.keys():
for name in favorate_languages.keys():
    print(name.title())

#3.按顺序遍历字典中所有键
#for 变量名 in sorted (字典变量名.keys()):
for name in sorted (favorate_languages.keys()):  #按字母先后顺序遍历
    print(name.title())

#4.遍历所有的值
#for 变量名 in 字典变量名.values():
for language in favorate_languages.values():
    print(language.title())

#5.按顺序遍历所有的值
#for 变量名 in sorted (字典变量名.values()):
for language in sorted (favorate_languages.values()):  #按字母先后顺序遍历
    print(language.title())