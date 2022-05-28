#创建数据地图和数据规划，以了解数据集的概况
#数据中存在以下潜在问题：
#重复变量，可能错误，丢失值，变量转换
import pandas as pd
import numpy as np
df = pd.DataFrame(
    {
        'A':[0,0,0,0,0,1,1],
        'B':[1,2,3,5,4,2,5],
        'C':[5,3,4,1,1,2,3]
    }
)  #A中0为第一个序列，1为第二个序列
#groupby()函数把集B,C放入组中，describe()函数获取统计信息
a_group_desc = df.groupby('A').describe()
unstacked = a_group_desc.unstack()  #unstack()函数创建了一种新的展示
print(unstacked.loc[:,['count','mean']])  #loc[]获取特定的条目

#给数据组添加元素
df = pd.DataFrame({
    'A':[2,3,1],
    'B':[1,2,3],
    'C':[5,3,4]
})
df1 = pd.DataFrame({
    'A':[4],
    'B':[4],
    'C':[4]
})
#横向添加
#方法1：利用append
df = df.append(df1)  #添加元素，但是此时索引未改变
print(df)
df = df.reset_index(drop=True)  #重置索引
print(df)
#方法2：结合loc和last_valid_index
df.loc[df.last_valid_index() + 1] = [5,5,5]  #last_valid_index()返回最后一排索引
print('\n')
print(df)
#纵向添加
#方法3：利用join
df2 = pd.DataFrame({
    'D':[1,2,3,4,5]
})
df = pd.DataFrame.join(df,df2)
print('\n')
print(df)

#利用索引移除数据
df = df.drop(df.index[[1,2]]) #横排移除
print('\n')
print(df)
df = df.drop('B',1)  #纵向移除
print('\n')
print(df)

#数组排序
df = pd.DataFrame({
    'A':[2,1,2,3,3,5,4],
    'B':[1,2,3,5,4,2,5],
    'C':[5,3,4,1,1,2,3]
})
#sort_values按列排序，先按'A'列升序排序，再按'B'列升序排序
#axis=1为按行排序，by对应行号数组
df = df.sort_values(by=['A','B'],axis=0,ascending=[True,True])
df = df.reset_index(drop=True)
print('\n')
print(df)

#数组随机化
index = df.index.to_list()  #获取现有索引
np.random.shuffle(index)  #随机化索引
df = df.loc[index] #将新索引顺序应用于df
df = df.reset_index(drop=True)
print('\n')
print(df)

#聚合数据（聚类）
df = pd.DataFrame({
    'Map':[0,0,0,1,1,2,2],
    'Values':[1,2,3,5,4,2,5]
})
df['S'] = df.groupby('Map')['Values'].transform(np.sum)
df['M'] = df.groupby('Map')['Values'].transform(np.mean)
df['V'] = df.groupby('Map')['Values'].transform(np.var)
print(df)