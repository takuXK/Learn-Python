from random import choice
class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points = num_points  #随机漫步默认点数为5000，即漫步5000次
        self.x_value = [0]  #每次漫步的初始点为(0,0)
        self.y_value = [0]
    def get_step(self):
        # 轴上的移动
        direction = choice([-1,1])  #移动方向
        distance = choice(range(0,5))  #移动距离
        step = direction * distance
        return step
    def fill_walk(self):
        while len(self.x_value) < self.num_points:  #漫步次数未达到5000次
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            #生成后续点坐标
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            #将新坐标加入坐标数组
            self.x_value.append(next_x)
            self.y_value.append(next_y)