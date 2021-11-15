# даны два целых числа A и B (A < B)
# вывести в порядке возрастания все целые числа, расположенные между A и B
# (включая сами числа A и B), а также количество N этих чисел

print('Введите числа a, b')
a, b = input('a = '), input('b = ')

while type(a) != int:  # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Введите целое число! ")
        a = input("a = ")

while type(b) != int:  # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Введите целое число! ")
        b = input("b = ")

while a >= b:  # обработка исключений
    print('Введите такие числа, чтобы a < b!')
    a, b = int(input('a = ')), int(input('b = '))

n = 0

while a != b + 1:  # вывод чисел и их подсчет
    print(a)
    a += 1
    n += 1

print('\nКоличество чисел =', n)
