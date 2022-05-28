#发现数据中的丢失项，并对丢失项作出响应
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
s = pd.Series([1,2,3,np.NaN,5,6,None])
#寻找丢失值
null_index = s.isnull()  #寻找NaN值序列位置
print(null_index)
print('\n')
null_value = s[s.isnull()]  #通过序列位置索引得到空值的结果
print(null_value)
#对丢失值进行处理
null_fill = s.fillna(int(s.mean()))  #利用s中有效值的平均值取整填充丢失值
print(null_fill)
print('\n')
null_drop = s.dropna()  #丢弃丢失值（序号不缩进）
print(null_drop)

X = [[np.nan, 2], [6, np.nan], [7, 6]]
imp = SimpleImputer(
    missing_values=np.nan,strategy='mean'
)  #创建一个评估器，查看寻找missing_values，代替丢失值方法为取平均
imp.fit([[1, 2], [np.nan, 3], [7, 6]])  #fit()提供SimpleImputer所使用的统计量
result = imp.transform(X)  #运用fit中数组按列的平均值代替NAN
print(result)
#另有一种fit_transform()但结果不同
result = imp.fit_transform(X)
print(result)