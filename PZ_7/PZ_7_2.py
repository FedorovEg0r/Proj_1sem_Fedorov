# Даны строки S, S1 и S2. Заменить в строке S последнее
# вхождение строки S1 на строку S2

s = str(input('Введите строку s: '))
s1 = str(input('Введите строку s1: '))
s2 = str(input('Введите строку s2: '))

s = s[:s.rfind(s1)] + s2 + s[s.rfind(s1) + len(s1):]  # изменение строки

print(s)