import numpy as np

dataset = np.array(
    [
        [2,4,6,8,3,2,5],
        [7,5,3,1,6,8,0],
        [1,3,2,1,0,0,8]
    ]
)
#各行/列 max-min 
res = np.max(dataset,axis=1) - np.min(dataset,axis=1)  #axis=0按列，axis=1按行
print(res)

#矩阵乘法
a = np.array(
    [
        [2,4,6,8],
        [1,3,5,7]
    ]

    )
b = np.array(
    [
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6],
        [4,5,6,7]
    ]
)
c = np.dot(a,b)
print(c)