'''Импортируем библиотку math для math.pi'''
import math

def area(r):
    '''Принимает R - радиус круга, возвращает площадь круга'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает R - радиус круга, возвращает длину окружности'''
    return 2 * math.pi * r


import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
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
        self.assertRaises(ValueError, area, -5)

    

    
