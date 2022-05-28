#创建分类变量：目录
#匹配目录
import pandas as pd
car_colors = pd.Series(['Blue','Red','Green'],dtype='category')  #创建可接受目录序列

car_data = pd.Series(
    pd.Categorical(['Yellow','Green','Red','Blue','Purple'],
    categories=car_colors,ordered=False)
)  #创建实际目录序列，匹配参数categories，若不存在，返回NaN

find_entries = pd.isnull(car_data)  #寻找NaN，输出对应空条目为True，反之为False

print(car_colors)
print('\n')
print(car_data)
print('\n')
print(find_entries)
print('\nunderline\n')

car_colors.cat.categories = ['Purple','Yellow','Mauve']  #改变了car_colors目录
print(car_colors)
car_data.cat.categories = car_colors
print(car_data)
###################################################################################
car_data = pd.Series(
    pd.Categorical(['Blue','Green','Red','Green','Red','Green'],
    categories=car_colors,ordered=False)
    )
car_data.cat.categories = ['Blue_Red','Red','Green']
print(car_data._ix[car_data.isin(['Red'])])

car_data._ix[car_data.isin(['Red'])] = 'Blue_Red'  #将'Red'条目改为'Blue_Red'
print('\n')
print(car_data)