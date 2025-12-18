
def area(a, h):
    if (a < 0 or h < 0):
        raise ValueError
    '''считает площадь треугольника на основании длин высоты и основания'''
    return a * h / 2


def perimeter(a, b, c):
    if (a < 0 or b < 0 or c < 0):
        raise ValueError
    '''считает периметр треугольника на основании длин сторон'''
    return a + b + c