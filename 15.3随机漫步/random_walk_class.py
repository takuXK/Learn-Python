#15.3
#随机漫步：随机决策决定的行走路径
#创建随机漫步类
from random import choice
#这里将使用choice()来决定使用哪种选择
class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points = num_points  #随机漫步默认点数为5000，即漫步5000次
        self.x_value = [0]  #每次漫步的初始点为(0,0)
        self.y_value = [0]
    def fill_walk(self):
        while len(self.x_value) < self.num_points:  #漫步次数未达到5000次
            # x轴上的移动
            x_direction = choice([-1,1])  #移动方向
            x_distance = choice(range(0,5))  #移动距离
            x_step = x_direction * x_distance
            # y轴上的移动
            y_direction = choice([-1,1])
            y_distance = choice(range(0,5))
            y_step = y_direction * y_distance
            # 保证没有原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #生成后续点坐标
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            #将新坐标加入坐标数组
            self.x_value.append(next_x)
            self.y_value.append(next_y)