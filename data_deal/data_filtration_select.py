#多维数组操作（矩阵切分、变换、连接）
import numpy as np
tri_D_matrix = [
    [[1,2,3],[4,5,6],[7,8,9],],
    [[10,11,12],[13,14,15],[16,17,18],],
    [[19,20,21],[22,23,24],[25,26,27],],
]
res = np.array(tri_D_matrix)
for i in range(3):
    print('print by row:')
    print(res[i,:])  #按行输出
    print('print by column:')
    print(res[:,i])  #按列输出
print('\n')
print(res[1,1])  #第二行第二列
print(res[:,1,1])  #第二列所有向量中第二个元素
print(res[1,:,1])  #第二行所有向量中第二个元素
print('\n')
print(res[1:3,1:3,1])  #第二、三行，第二、三列向量中第二个元素