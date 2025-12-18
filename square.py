def area(a):
    if (a < 0):
        raise ValueError
    '''Принимает a сторону квадрата, возвращает площадь квадрата'''
    return a * a


def perimeter(a):
    if (a < 0):
        raise ValueError
    '''Принимает a сторону квадрата, возвращает периметр квадрата'''
    return 4 * a