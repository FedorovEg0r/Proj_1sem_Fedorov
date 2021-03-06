# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти среднее значение продаж по
# каждому виду продукции, результаты вывести на экран


def average(dct):  # вычисление среднего значения
    q = 0
    sm = 0
    while q != 5:
        sm += int(list(dct.values())[0][q])
        q += 1
    avg = sm/5
    return avg


s = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
lst = s.split(' ')  # преобразование строки s в список

a, b = ['x'] * 5, ['x'] * 5  # создание списков
i = 1  # счетчик
while i != 6:  # заполнение списков
    a[i-1] = lst[i]
    b[i-1] = lst[i+6]
    i += 1

da = {'апельсины': a}  # создание словарей
db = {'яблоки': b}

print(da)
print(db)

da_avg = average(da)  # поиск средних значений
db_avg = average(db)

print('Среднее количество продаж апельсинов в кг:', da_avg)
print('Среднее количество продаж яблок в кг:', db_avg)
