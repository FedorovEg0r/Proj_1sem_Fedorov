from tkinter import *
root = Tk()
root.title('PZ_12_1')
root.geometry('510x425')
frame1 = Frame(root, bg='deepskyblue', bd=1)
label1 = Label(frame1, text='Форма заявки', width=60, height=1, bg='seagreen',
               fg='white', font='agency 14')
frame1.pack()
label1.pack()
frame2 = Frame(root, bg='deepskyblue', bd=1)
label2 = Label(frame2, text='Допустимые типы вложений: zip, rar, txt, doc, '
                            'jpg, png, gif, odt, xml                       '
                            '  \n Макс. размер каждого файла: 1024kb.      '
                            '                                              '
                            '                \n Макс. общий размер файла: 2'
                            '048kb.                                        '
                            '                              ', width=80,
               height=3, bg='gainsboro', fg='black', font='arial 10')
frame2.pack()
label2.pack()
frame3 = Frame(root, bg='deepskyblue', bd=1)
frame4 = Frame(root, bg='deepskyblue', bd=1)
frame5 = Frame(root, bg='deepskyblue', bd=1)
frame6 = Frame(root, bg='deepskyblue', bd=1)
frame7 = Frame(root, bg='deepskyblue', bd=1)
frame8 = Frame(root, bg='deepskyblue', bd=1)
label3 = Label(frame3, text='    Ваше имя:                     ', width=18,
               height=1, bg='gainsboro', fg='black', font='arial 13')
label4 = Label(frame4, text='    Ваш Email:                     ', width=18,
               height=1, bg='gainsboro', fg='black', font='arial 13')
label5 = Label(frame5, text='    Тема письма:                ', width=18,
               height=1, bg='gainsboro', fg='black', font='arial 13')
label6 = Label(frame6, text='    Прикрепить файл:         ', width=18,
               height=1, bg='gainsboro', fg='black', font='arial 13')
label7 = Label(frame7, text='    Прикрепить файл:         ', width=18,
               height=1, bg='gainsboro', fg='black', font='arial 13')
label8 = Label(frame8, text='    Прикрепить файл:         ', width=18,
               height=1, bg='gainsboro', fg='black', font='arial 13')
frame3.place(x=0, y=85)
label3.pack()
frame4.place(x=0, y=111)
label4.pack()
frame5.place(x=0, y=137)
label5.pack()
frame6.place(x=0, y=163)
label6.pack()
frame7.place(x=0, y=189)
label7.pack()
frame8.place(x=0, y=215)
label8.pack()
frame9 = Frame(root, bg='deepskyblue', bd=1)
frame10 = Frame(root, bg='deepskyblue', bd=1)
frame11 = Frame(root, bg='deepskyblue', bd=1)
frame12 = Frame(root, bg='deepskyblue', bd=1)
frame13 = Frame(root, bg='deepskyblue', bd=1)
frame14 = Frame(root, bg='deepskyblue', bd=1)
frame9.place(x=169, y=85, width=341, height=26)
frame10.place(x=169, y=111, width=341, height=26)
frame11.place(x=169, y=137, width=341, height=26)
frame12.place(x=169, y=163, width=341, height=26)
frame13.place(x=169, y=189, width=341, height=26)
frame14.place(x=169, y=215, width=341, height=26)
entry1 = Entry(frame9, font='default 21')
entry1.place(width=200, height=26)
entry2 = Entry(frame10, font='default 21')
entry2.place(width=200, height=26)
entry3 = Entry(frame11, font='default 21')
entry3.place(width=200, height=26)
entry4 = Entry(frame12, font='default 21')
entry4.place(width=200, height=26)
entry5 = Entry(frame13, font='default 21')
entry5.place(width=200, height=26)
entry6 = Entry(frame14, font='default 21')
entry6.place(width=200, height=26)
frame15 = Frame(root, bg='gainsboro', bd=1)
frame15.place(x=371, y=86, width=141, height=25)
label9 = Label(frame15, text='*                      ', bg='gainsboro',
               fg='red', height=26, width=141, font='arial 15')
label9.pack()
frame16 = Frame(root, bg='gainsboro', bd=1)
frame16.place(x=371, y=112, width=141, height=25)
label10 = Label(frame16, text='*                      ', bg='gainsboro',
                fg='red', height=26, width=141, font='arial 15')
label10.pack()
frame17 = Frame(root, bg='gainsboro', bd=1)
frame17.place(x=371, y=138, width=141, height=25)
label11 = Label(frame17, text='', bg='gainsboro', fg='red', height=26,
                width=141)
label11.pack()
frame18 = Frame(root, bg='gainsboro', bd=1)
frame18.place(x=371, y=164, width=141, height=25)
label12 = Label(frame18, text='', bg='gainsboro', fg='red', height=26,
                width=141)
label12.pack()
frame19 = Frame(root, bg='gainsboro', bd=1)
frame19.place(x=371, y=190, width=141, height=25)
label13 = Label(frame19, text='', bg='gainsboro', fg='red', height=26,
                width=141)
label13.pack()
frame20 = Frame(root, bg='gainsboro', bd=1)
frame20.place(x=371, y=216, width=141, height=25)
label13 = Label(frame20, text='', bg='gainsboro', fg='red', height=26,
                width=141)
label13.pack()
button1 = Button(root, text='Обзор...', bg='ghost white', fg='black',
                 font='arial 9')
button1.place(x=373, y=166, width=80, height=20)
button2 = Button(root, text='Обзор...', bg='ghost white', fg='black',
                 font='arial 9')
button2.place(x=373, y=192, width=80, height=20)
button3 = Button(root, text='Обзор...', bg='ghost white', fg='black',
                 font='arial 9')
button3.place(x=373, y=218, width=80, height=20)
frame21 = Frame(root, bg='deepskyblue', bd=1)
frame21.place(x=0, y=241, width=510, height=155)
label14 = Label(frame21, text='', bg='gainsboro', height=145, width=510)
label14.pack()
label15 = Label(root, text='Ваше сообщение:', bg='gainsboro', fg='black',
                font='arial 11')
label15.place(x=1, y=242)
label16 = Label(root, text='*', bg='gainsboro', fg='red', font='arial 11')
label16.place(x=125, y=242)
frame22 = Frame(root, bg='deepskyblue', bd=1)
frame22.place(x=40, y=265, width=430, height=125)
scrollbar = Scrollbar(frame22)
scrollbar.pack(side='right', fill=Y)
text = Text(frame22, height=125, width=430, wrap=WORD)
Text.pack(self=text)
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
frame23 = Frame(root, bg='black', bd=1)
frame23.place(x=0, y=396, width=510, height=29)
label17 = Label(frame23, text='', bg='seagreen', width=510, height=29)
label17.pack()
button4 = Button(root, text='Отправить Email ', bg='ghost white', fg='black',
                 font='arial 10')
button4.place(x=135, y=400, width=135, height=20)
button5 = Button(root, text='Очистить', bg='ghost white', fg='black',
                 font='arial 10', command=lambda: text.delete('1.0', END))
button5.place(x=282, y=400, width=95, height=20)
root.mainloop()
