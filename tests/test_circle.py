from circle import area, perimeter

import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(10)
        self.assertEqual(res, 100 * math.pi)
    
    def test_negative_area(self):
        self.assertRaises(ValueError, area, -5)

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_per(self):
        res = perimeter(10)
        self.assertEqual(res, 20 * math.pi)

    def test_negative_per(self):
        self.assertRaises(ValueError, perimeter, -5)
