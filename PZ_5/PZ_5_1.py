# найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование
# оформить функцией с параметрами. Значения n и m программа должна запрашивать


def Summ(n, m):  # описание функции
    s = 0
    while n != m + 1:
        s += n
        n += 1
    return s

n = int(input('Введите первое число: '))  # ввод чисел
m = int(input('Введите второе число: '))

print('Сумма чисел ряда от n до m =', Summ(n, m))  # вывод результата
