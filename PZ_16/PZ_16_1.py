import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#b5feff', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="gif/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить пациента', command=self.open_dialog, bg='#1689f0', bd=0,
                                    compound=tk.TOP, image=self.add_img, width=158, height=40)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="gif/12.gif")
        self.btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#1689f0',
                                    bd=0, compound=tk.TOP, image=self.update_img, width=158, height=40)
        self.btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="gif/13.gif")
        self.btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#1689f0',
                                    bd=0, compound=tk.TOP, image=self.delete_img, width=158, height=40)
        self.btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="gif/14.gif")
        self.btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#1689f0',
                               bd=0, compound=tk.TOP, image=self.search_img, width=158, height=40)
        self.btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="gif/15.gif")
        self.btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#1689f0',
                               bd=0, compound=tk.TOP, image=self.refresh_img, width=158, height=40)
        self.btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('id', 'pat_fio', 'doc_fio', 'diagnosis', 'cost'), height=19, show='headings')

        self.tree.column('id', width=40, anchor=tk.CENTER)
        self.tree.column('pat_fio', width=230, anchor=tk.CENTER)
        self.tree.column('doc_fio', width=230, anchor=tk.CENTER)
        self.tree.column('diagnosis', width=166, anchor=tk.CENTER)
        self.tree.column('cost', width=125, anchor=tk.CENTER)

        self.tree.heading('id', text='ID')
        self.tree.heading('pat_fio', text='ФИО пациента')
        self.tree.heading('doc_fio', text='ФИО врача')
        self.tree.heading('diagnosis', text='Диагноз')
        self.tree.heading('cost', text='Стоимость лечения')

        self.tree.pack()

    def records(self, id, pat_fio, doc_fio, diagnosis, cost):
        self.db.insert_data(id, pat_fio, doc_fio, diagnosis, cost)
        self.view_records()

    def update_record(self, id, pat_fio, doc_fio, diagnosis, cost):
        self.db.cur.execute("""UPDATE patients SET id=?, pat_fio=?, doc_fio=?, diagnosis=?, cost=? WHERE id=?""",
                            (id, pat_fio, doc_fio, diagnosis, cost, self.tree.set(self.tree.selection()[0], '#1'),))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM patients""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM patients WHERE id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, score):
        score = (score,)
        self.db.cur.execute("""SELECT * FROM patients WHERE cost=?""", score)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить пациента')
        self.geometry('400x220+580+300')
        self.resizable(False, False)

        label_id = tk.Label(self, text='ID')
        label_id.place(x=50, y=25)
        self.entry_id = ttk.Entry(self, width=33)
        self.entry_id.place(x=175, y=25)

        label_pat_fio = tk.Label(self, text='ФИО пациента')
        label_pat_fio.place(x=50, y=50)
        self.entry_pat_fio = ttk.Entry(self, width=33)
        self.entry_pat_fio.place(x=175, y=50)

        label_doc_fio = tk.Label(self, text='ФИО врача')
        label_doc_fio.place(x=50, y=75)
        self.entry_doc_fio = ttk.Entry(self, width=33)
        self.entry_doc_fio.place(x=175, y=75)

        label_diagnosis = tk.Label(self, text='Диагноз')
        label_diagnosis.place(x=50, y=100)
        self.entry_diagnosis = ttk.Entry(self, width=33)
        self.entry_diagnosis.place(x=175, y=100)

        label_cost = tk.Label(self, text='Стоимость лечения')
        label_cost.place(x=50, y=125)
        self.entry_cost = ttk.Entry(self, width=33)
        self.entry_cost.place(x=175, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=305, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=225, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_id.get(),
                                                                       self.entry_pat_fio.get(),
                                                                       self.entry_doc_fio.get(),
                                                                       self.entry_diagnosis.get(),
                                                                       self.entry_cost.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=210, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_id.get(),
                                                                          self.entry_pat_fio.get(),
                                                                          self.entry_doc_fio.get(),
                                                                          self.entry_diagnosis.get(),
                                                                          self.entry_cost.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("430x100+550+350")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск (найдет записи по точной\nстоимости лечения)")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=255, y=20, width=155)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=335, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=255, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('patient.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS patients (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     pat_fio TEXT NOT NULL,
                     doc_fio TEXT NOT NULL,
                     diagnosis TEXT NOT NULL,
                     cost INTEGER
                 )""")

    def insert_data(self, id, pat_fio, doc_fio, diagnosis, cost):
        self.cur.execute("""INSERT INTO patients(id, pat_fio, doc_fio, diagnosis, cost) VALUES (?, ?, ?, ?, ?)""",
                             (id, pat_fio, doc_fio, diagnosis, cost))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Платная поликлиника")
    root.geometry("802x463+350+175")
    root.resizable(False, False)
    root.mainloop()
