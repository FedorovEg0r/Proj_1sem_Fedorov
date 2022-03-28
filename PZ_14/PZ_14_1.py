#  в исходном текстовом файле (Dostoevsky.txt) найти все произведения писателя.
#  посчитать количество полученных элементов.

import re

# поиск произведений в файле
with open('Dostoevsky.txt', encoding="utf-8") as f:
    text = f.read()
res = re.findall(r"«[^ЕВЭд].*?»", text)

# преобразование списка произведений и их подсчет
res.sort()
res = list(set(res))
res.sort()
k = len(res)
res = ',\n'.join(map(str, res))

# вывод результатов
print("Произведения писателя, встречающиеся в тексте:\n", res, sep='')
print("\nЧисло произведений писателя, упомянутых в тексте:", k)
