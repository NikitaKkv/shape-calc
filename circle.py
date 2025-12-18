'''Импортируем библиотку math для math.pi'''
import math

def area(r):
    if (r < 0):
        raise ValueError
    '''Принимает R - радиус круга, возвращает площадь круга'''
    return math.pi * r * r


def perimeter(r):
    if (r < 0):
        raise ValueError
    '''Принимает R - радиус круга, возвращает длину окружности'''
    return 2 * math.pi * r