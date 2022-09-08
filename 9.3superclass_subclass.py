#9.3
#需要的类（子类）是现有类（父类）的特殊版本，子类继承父类时，将自动获得父类的所有属性和方法
class Car():  #父类
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        total = self.make + ' ' + self.model + ' ' + str(self.year)
        return total.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
    def increment_odometre(self,miles):
        if miles > 0:
            self.odometer_reading += miles
    def fill_gas_tank(self):
        print('Gas has been filled!')
#定义子类，需在括号内指定父类的名称：class 子类名(父类名):
class ElectricCar(Car):  #子类 
    def __init__(self,make,model,year):  #__init__方法接受创建Car实例所需的信息
        super().__init__(make,model,year)  #super函数将子类和父类关联起来
    #以上为止已经继承父类，下面开始定义子类特有属性和方法(电池容量)
        self.battery_size = 70  #注意定义新属性均与super语句对齐，父类并不包含该属性
    def describe_battery(self):  #方法正常定义
        print('Remain ' + str(self.battery_size) +"-KWh.")
    def set_battery(self,remain):
        if remain <= self.battery_size:
            self.battery_size = remain
    def decrease_battery(self,des):
        if des >= 0:
            self.battery_size -= des
    def fill_gas_tank(self):
        #父类也存在一个同名方法，然而加油对电动汽车毫无意义，当子类和父类存在同名方法时，python只运行子类中那个
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.set_battery(60)
my_tesla.describe_battery()
my_tesla.decrease_battery(5)
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

#有时我们在定义子类的时候发现子类的方法往往和子类的某一部分零件有关
#如上述示例中子类电动汽车的大多数方法都和电池有关，此时我们可以定义一个无关联新类（辅助类）：
class Battery():  #辅助类
    def __init__(self,battery_size=70):  #battery_size为可选择输入变量
        self.battery_size = battery_size
    def describe_battery(self):
        print('Remain ' + str(self.battery_size) +"-KWh.")
    def get_range(self,battery_size):
        range = 3*battery_size
        print("This car can go approximately " + str(range) + " miles on full charge.")
class ElectricalCar(Car):  #子类 
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery() #此处连接两个类，创建了一个Battery示例，故Battery类一定要写在ElectricalCar前
print('\n')
my_tesla = ElectricalCar('tesla','model s',2016)
my_tesla.battery.describe_battery()  #调用格式：实例名.子类属性名.辅助类方法
my_tesla.battery.get_range(60)