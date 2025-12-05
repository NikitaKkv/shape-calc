# Математические формулы
## Площадь
- Круг: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²

## Периметр
- Круг: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a

# Общее описание
Реализация нахождения площадей и периметров для разных фигур

# Функции
## circle.py
- area(r) - считает площадь круга в зависимости от радиуса круга
  - area(1) = 3.141592653589793
  - area(2) = 12.566370614359172
- perimeter(r) - считает длину окружности в зависимости от радиуса окружности
  - perimeter(1) = 6.283185307179586
  - perimeter(2) = 12.566370614359172

## square.py
- area(a) - считает площадь квадрата на основании длины стороны квадрата
  - area(1) = 1
  - area(3) = 9
- perimeter(a) - считает периметр квадрата на основании длины стрроны квадрата
  - perimeter(2) = 8
  - perimeter(3) = 12

# Удаленные функции

## rectangle.py
- area(a, b) - считает площадь прямоугольника на основании длин соседних сторон
  - area(1, 2) = 2
  - area(3, 4) = 12
- perimeter(a, b) - считает периметр прямоугольника на основании длин соседних сторон
  - perimeter(2, 3) = 10
  - perimeter(5, 3) = 16

## triangle.py
- area(a, h) - считает площадь треугольника на основании длин стороны и ее высоты
  - area(2, 3) = 3
  - area(5, 4) = 10
- perimeter(a, b, c) - считает периметр треугольника на основании длин сторон треугольника
  - perimeter(2, 3, 2) = 7
  - perimeter(5, 3, 2) = 10

# История изменений проекта

* 438b89a L-05: Add user agreement  
* 6adb962 L-03: Docs added  
| * 3049431 (origin/feature) L-04: Add rectangle.py  
| | * b5b0fae (origin/develop) L-04: Update docs for calculate.py  
| | * d76db2a L-04: Add calculate.py  
| | * 51c40eb L-04: Doc updated for triangle  
| | * d080c78 L-04: Triangle added  
| |/   
| * d078c8d (HEAD -> main, origin/main, origin/HEAD) L-03: Docs   added  
|/    
* 8ba9aeb L-03: Circle and square added  
