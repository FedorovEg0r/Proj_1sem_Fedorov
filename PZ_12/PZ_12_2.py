# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.

from tkinter import *


def gettextinput():
    result = text1.get("1.0", "end")
    return result


def ans(n):
    while n > 1:
        n = n / 3

    if n == 1.0:
        a = 'TRUE'
    else:
        a = 'FALSE'
    label3 = Label(root, text='')
    label3.place(x=10, y=70)
    label3.config(text="Ответ: {}".format(a))


root = Tk()
root.title('PZ_12_2')
root.geometry('670x100')

label1 = Label(root,
               text='Дано целое число N (>0). Если оно является степенью числа'
                    ' 3, то вывести TRUE, если не является — вывести FALSE',)
label1.place(x=10, y=5)
label2 = Label(root, text='Введите целое число N (>0):')
label2.place(x=10, y=40)
text1 = Text(root)
text1.place(x=170, y=43, width=80, height=17)
button1 = Button(root, text='Вычислить',
                 command=lambda: ans(int(gettextinput())))
button1.place(x=260, y=43, width=80, height=17)

root.mainloop()
