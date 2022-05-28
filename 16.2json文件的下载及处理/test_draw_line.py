from draw_function import draw_line
import unittest
class TestDrawFunction(unittest.TestCase):
    def test_draw_function(self):
        line_image = draw_line([1,2,3],[1,4,9],'image of square','value of square')
        self.assertEqual(line_image.x_labels , [1,2,3])
unittest.main() 