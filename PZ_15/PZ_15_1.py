# В матрице найти сумму элементов второй половины матрицы

from random import randint

m = int(input('Введите количество строк матрицы: '))
n = int(input('Введите количество столбцов матрицы: '))

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

# подсчет суммы элементов второй половины матрицы
s = 0
print('\nВторая половина матрицы:')
for i in range(round(m/2), m):
    for k in range(n):
        s += int(A[i][k])
        if k == n-1:
            print(A[i])

print('\nСумма элементов второй половины матрицы =', s)
