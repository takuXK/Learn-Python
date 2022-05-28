from random import randint
import os
class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        result = randint(1,self.num_sides)
        return result

import pygal
die1 = Die()
die2 = Die(10)
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist._title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = [
    '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'
]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add('D6 + D10',frequencies)
os.chdir('D:\\python\\vs python work\\15.2简单图像')
hist.render_to_file('dice_visual.svg')