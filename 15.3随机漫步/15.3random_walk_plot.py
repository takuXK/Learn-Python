import matplotlib.pyplot as plt
from random_walk_class_1 import RandomWalk
while True:  #在关闭plot窗口时询问是否再次生成一个随机漫步
    my_random_walk = RandomWalk(5000)
    my_random_walk.fill_walk()
    colors = list(range(my_random_walk.num_points))
    #创建图像框大小(英寸)和分辨率
    plt.figure(dpi=128,figsize=(10,6))
    plt.scatter(my_random_walk.x_value,my_random_walk.y_value,
        c=colors,cmap=plt.cm.Blues,edgecolors='none',s=1)
    #隐藏坐标轴
    plt.axis('off')
    plt.show()
    make_another = input("Make another walk?(yes/no)")
    if make_another == 'no':
        break