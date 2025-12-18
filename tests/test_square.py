from square import area, perimeter

import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(10)
        self.assertEqual(res, 100)
    
    def test_negative_area(self):
        self.assertRaises(ValueError, area, -5)
    
    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_per(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_negative_per(self):
        self.assertRaises(ValueError, perimeter, -5)