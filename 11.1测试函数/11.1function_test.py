#11.1
#函数测试用例步骤
#1.导入模块unittest和要测试的函数
#2.创建一个继承unittest.TestCase的类
#3.在类中编写一系列方法对函数进行不同方面的测试
import unittest
from name_function import get_formatted_name
class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):  #测试无中间名时函数的有效性
        formatted_name = get_formatted_name('janis','joplin')
        #self.assertEqual(实际结果,期望结果)，断言方法，用来核实得到的结果是否与期望的结果一致
        #另外还有assertNotEqual,assertTrue等断言方法
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
unittest.main()  #运行测试