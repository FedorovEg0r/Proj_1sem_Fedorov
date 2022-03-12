# В матрице элементы второго столбца возвести в квадрат

from random import randint

m = int(input('Введите количество строк матрицы: '))
n = int(input('Введите количество столбцов матрицы (>=2): '))

# обработка исключений
while n < 2:
    n = int(input('Введите количество столбцов матрицы (>=2): '))

# создание матрицы
A = [0] * m

print('\nВаша матрица:')
for i in range(m):
    A[i] = [0] * n

for i in range(m):
    for k in range(n):
        A[i][k] = randint(-10, 10)
        if k == n-1:
            print(A[i])

# возведение в квадрат элементов второго столбца
for i in range(m):
    A[i][1] = A[i][1] ** 2

# вывод результата
print('\nМатрица после изменений:')
for i in range(m):
    for k in range(n):
        if k == n-1:
            print(A[i])
