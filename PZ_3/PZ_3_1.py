# даны числа х, у. Проверить истинность высказывания:
# «Точка с координатами (х, у) лежит во второй координатной четверти»

print("Введите координаты точки x и y")
x, y = input("x = "), input("y = ")

while type(x) != float:  # обработка исключений
    try:
        x = float(x)
    except ValueError:
        print("Введите число! ")
        x = input("x = ")

while type(y) != float:  # обработка исключений
    try:
        y = float(y)
    except ValueError:
        print("Введите число! ")
        y = input("y = ")

if x < 0 and y > 0:  # проверка истинности утверждения
    print('Утверждение верно')
else:
    print('Утверждение неверно')
