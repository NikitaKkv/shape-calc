def area(a, b):
    if (a < 0 or b < 0):
        raise ValueError
    '''считает площадь прямоугольника на основании длин соседних сторон'''
    return a * b


def perimeter(a, b):
    if (a < 0 or b < 0):
        raise ValueError
    '''считает периметр прямоугольника на основании длин соседних сторон'''
    return 2 * (a + b)
