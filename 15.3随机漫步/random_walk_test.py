#测试随机漫步
import unittest
from random_walk_class import RandomWalk
class RandomWalkTest(unittest.TestCase):
    def testrandomwalk(self):
        my_randomwalk = RandomWalk(2)
        my_randomwalk.fill_walk()
        self.assertTrue(len(my_randomwalk.x_value) == 2 and len(my_randomwalk.y_value) == 2)
unittest.main()