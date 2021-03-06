# Даны множества A и B, состоящие соответственно из N1 и N2 точек (точки заданы
# своими координатами x, у). Найти минимальное расстояние между точками этих
# множеств и сами точки, расположенные на этом расстоянии (вначале выводится
# точка из множества A, затем точка из множества B).
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется
# по формуле: R = √((x2 – x1)^2 + (у2 – y1)^2)
# Для хранения данных о каждом наборе точек следует использовать по два списка:
# первый список для хранения абсцисс, второй — для хранения ординат


from math import sqrt

n1 = int(input('Введите количество точек множества А: '))
n2 = int(input('Введите количество точек множества B: '))
ax, bx = ['n'] * n1, ['n'] * n2  # создание спиков абсцисс
ay, by = ['n'] * n1, ['n'] * n2  # создание спиков ординат

i = 0  # счетчик
print('\nЗаполнение списка абсцисс множества А')
while i != n1:  # заполнение списка
    ax[i] = int(input('Введите число: '))
    i += 1

i = 0  # обнуление счетчика
print('\nЗаполнение списка ординат множества А')
while i != n1:  # заполнение списка
    ay[i] = int(input('Введите число: '))
    i += 1

i = 0  # обнуление счетчика
print('\nЗаполнение списка абсцисс множества B')
while i != n2:  # заполнение списка
    bx[i] = int(input('Введите число: '))
    i += 1

i = 0  # обнуление счетчика
print('\nЗаполнение списка ординат множества B')
while i != n2:  # заполнение списка
    by[i] = int(input('Введите число: '))
    i += 1

i = 0
k = 0
c = 0
r = sqrt((int(bx[k]) - int(ax[i])) ** 2 + (int(by[k]) - int(ay[i])) ** 2)
ia = 0
ib = 0
while i != n1:
    while k != n2:
        r = sqrt((int(bx[k]) - int(ax[i])) ** 2 + (int(by[k]) - int(ay[i])) ** 2)
        if r < c:
            c = r
            axz, ayz, bxz, byz = ax[i], ay[i], bx[k], by[k]
            ia = i
            ib = k
        k += 1
    i += 1

i = 0
k = 0
while i != n2:
    while k != n1:
        r = sqrt((int(bx[i]) - int(ax[k])) ** 2 + (int(by[i]) - int(ay[k])) ** 2)
        if r > c:
            c = r
            axz, ayz, bxz, byz = ax[k], ay[k], bx[i], by[i]
            ia = k
            ib = i
        k += 1
    i += 1

print('\nНаименьшее расстояние между точками =', c)
print('\nЭти точки: А[', ia, '](', axz, ';', ayz, ') B[',
      ib, '](', bxz, ';', byz, ')', sep='')
