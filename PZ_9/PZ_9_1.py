# Туристические агентства предлагают следующие туры. Вояж – Мексика,
# Канада,Израиль,Италия . РейнаТур – Англия,Япония,Канада,ЮАР. Определить:
# 1. какие туры из Вояж, отсутствуют в РейнаТур.
# 2. какие товары из РейнаТур, отсутствуют в Вояж
# 3. перечень одинаковых туров.
# 4. равны ли перечни туров


v = {'Мексика', 'Канада', 'Израиль', 'Италия'}  # объявление множеств
r = {'ЮАР', 'Англия', 'Япония', 'Канада'}

print('Туры Вояж:', v)  # вывод результатов
print('Туры РейнаТур:', r)
print('Туры из Вояж, которых нет в РейнаТур:', v-r)
print('Туры из РейнаТур, которых нет в Вояж:', r-v)
print('Перечень одинаковых туров:', v & r)
print('Равны ли перечни туров:', v == r)
