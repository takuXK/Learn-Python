#9.3
#使用类和实例
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  #在__init__方法中定义了初始值，则为默认值属性，无需在方法名后加入对应形参
    def get_descriptive_name(self):
        total = self.make + ' ' + self.model + ' ' + str(self.year)
        return total.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:  #禁止回调里程表
            self.odometer_reading = mileage
    def increment_odometre(self,miles):
        if miles > 0:  #禁止回调里程表
            self.odometer_reading += miles

my_car = Car('audi','a4',2020)
print(my_car.get_descriptive_name())
my_car.read_odometer()

#修改属性的值
#1.直接修改属性的值
my_car.odometer_reading = 23
my_car.read_odometer()
#2.通过方法修改属性的值
#见def update_odometer
my_car.update_odometer(45)  #此时update_odometer必须>=23
my_car.read_odometer()
#3.通过方法增加属性的值
#见def increment_odometre
old_car = Car('subaru','outback',2015)
print(old_car.get_descriptive_name())
old_car.update_odometer(23450)
old_car.read_odometer()
old_car.increment_odometre(100)
old_car.read_odometer()