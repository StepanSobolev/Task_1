from tkinter import *
import sqlite3
import tkinter as tk

# from main import new_member


db = sqlite3.connect('base.db')
cur = db.cursor()
root = Tk()
root.title('Програма')
root.geometry('600x300')
Label(root, text='Програма обліку зброї').grid(row=0, column=0, columnspan=4, sticky='we')


def register_pool():
    Label(root, text='Ім\'я').grid(row=2, column=0)
    name = Entry(root)
    name.grid(row=2, column=1)

    Label(root, text='Прізвище').grid(row=3, column=0)
    surname = Entry(root)
    surname.grid(row=3, column=1)

    Label(root, text='Номер').grid(row=4, column=0)
    number = Entry(root)
    number.grid(row=4, column=1)

    Label(root, text='Підрозділ').grid(row=5, column=0)
    subdivision = Entry(root)
    subdivision.grid(row=5, column=1)
    main_ok()


def main_ok():
    Button(root, text='OK', command=ak).grid(row=6, column=1)


def ak():
    choice = 'weapoons_ak'
    register_pool()
    # new_member(choice, name, surname, number, subdivision)


def pm():
    choice = 'weapoons_pm'
    # new_member(choice, name, surname, number, subdivision)


def new_member(table, name, surname, number, subdivision):
    name = name.get()
    surname = surname.get()
    number = number.get()
    subdivision = subdivision.get()
    cur.execute(f"""INSERT INTO {table} VALUES (?, ?, ?, ?)""", (name, surname, number, subdivision))
    db.commit()
    print('Данние успешно внесен')


Button(root, text='Додати Автомат', command=ak).grid(row=1, column=1)
Button(root, text='Додати Пістолет', command=pm).grid(row=1, column=2)
Button(root, text='Вихід', command=lambda: root.destroy()).grid(row=1, column=3)

root.mainloop()
