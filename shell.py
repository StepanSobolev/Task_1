from tkinter import *
import sqlite3


db = sqlite3.connect('base.db')
cur = db.cursor()
root = Tk()
root.title('Програма')
root.geometry('600x300')
Label(root, text='Програма обліку зброї').grid(row=0, column=0, columnspan=4, sticky='we')


def lable_enrty(changes, row, column):
    Label(root, text=f'{changes}').grid(row=row, column=column)
    chang = Entry(root)
    chang.grid(row=row, column=column + 1)
    return chang


def main_ok(choice, name, surname, number, subdivision):
    Button(root, text='OK',
           command=lambda choice=choice, name=name, surname=surname, number=number, subdivision=subdivision:
           new_member(choice, name, surname, number, subdivision)).grid(row=6, column=1)


def ak():
    choice = 'weapoons_ak'
    name = lable_enrty('Ім\'я', 2, 0)
    surname = lable_enrty('Прізвище', 3, 0)
    number = lable_enrty('Номер АК', 4, 0)
    subdivision = lable_enrty('Підрозділ', 5, 0)
    main_ok(choice, name, surname, number, subdivision)


def pm():
    choice = 'weapoons_pm'
    name = lable_enrty('Ім\'я', 2, 0)
    surname = lable_enrty('Прізвище', 3, 0)
    number = lable_enrty('Номер ПМ', 4, 0)
    subdivision = lable_enrty('Підрозділ', 5, 0)
    main_ok(choice, name, surname, number, subdivision)


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
