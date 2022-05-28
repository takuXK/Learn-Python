#11.2
#类测试用例步骤
#1.导入模块unittest和要测试的类
#2.创建一个继承unittest.TestCase的类
#3.在类中编写一系列方法对类进行不同方面的测试
import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):  #核实存储一个答案的情况
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)
    def test_store_three_response(self):  #核实存储三个答案的情况
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
unittest.main()

#上述测试在每个方法中都创建了实例和答案，方法setUp()将优先执行，可统一创建实例和答案共其它所有方法使用
class TestAnonymousSurvey2(unittest.TestCase):
    def setUp(self):
        question = 'What language did you first learn to speak?'
        self.survey2 = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
    def test_store_single_response2(self):
        self.survey2.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.survey2.responses)
    def test_store_three_response2(self):
        for response in self.responses:
            self.survey2.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.survey2.responses)
unittest.main()