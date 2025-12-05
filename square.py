def area(a):
    '''Принимает a сторону квадрата, возвращает площадь квадрата'''
    return a * a


def perimeter(a):
    '''Принимает a сторону квадрата, возвращает периметр квадрата'''
    return 4 * a



import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10)
       self.assertEqual(res, 100)
    
    def test_zero_per(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
    
    def test_per(self):
       res = perimeter(10)
       self.assertEqual(res, 40)

    