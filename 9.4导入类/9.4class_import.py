#9.4
#导入类，python允许从外部导入类
#导入单个类 from 模块名 import 类名
from car import Car
my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#导入多个类 from 模块名 import 类名1,类名2,...
from car import Car,ElectricCar
my_tesla = ElectricCar('tesla','model s',2016)
my_tesla.battery.get_range(60)  #虽然没有导入辅助类，但辅助类仍然可以使用

#导入整个模块中的所有类
#1.import 模块名：调用时要 模块名.类名
import car
my_beetle = car.Car('volkswagen','beetle',2018)
print(my_beetle.get_descriptive_name())
#2.from 模块名 import *

#在一个类中导入其他模块中的类
from car import Car
class ElectricalCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
    def get_battery(self,battery_size=70):
        self.battery = battery_size
        print("remain " + str(self.battery) + "-KWh.")
print('\n')
my_car = ElectricalCar('tesla','model c',2019)
my_car.get_battery(60)