#9.1
#创建类(class)：class 类名称(): (类的名称首字母大写)
class Dog():
    def __init__(self,name,age): #def _默认方法名_(传递名,属性名1,属性名2,...)
        #类中的函数被称为方法，前后两条下划线_代表该方法是默认方法，每当根据该类创建新实例时，该方法都会被自动运行
        #方法中self形参必不可少，且必须位于其他形参前，self会在类中自动传递
        self.name = name  #获取形参name中的值，并存储在变量name中，name为属性，类中的每个属性必须有初始值
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + ' roll over!')

#调用类创建实例
my_dog = Dog('willie',6)  #实例名 = 类名(属性名1,属性名2,...)
print("My dog's name is " + my_dog.name.title() + '.')  #访问属性：实例名.属性名
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()  #调用方法：实例名.方法名
my_dog.roll_over()