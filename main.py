import sqlite3
from shell import name, surname, number, subdivision

db = sqlite3.connect('base.db')
cur = db.cursor()



def new_member(table, name, surname, number, subdivision):
    name = name.get()
    surname = surname.get()
    number = number.get()
    subdivision = subdivision.get()
    cur.execute(f"""INSERT INTO {table} VALUES (?, ?, ?, ?)""", (name, surname, number, subdivision))
    db.commit()
    print('Данние успешно внесен')


def user_choice():
    choice = input('Что хотите зарегестировать\nавтомат нажми (А)'
                   '\nпистолет нажми (П)'
                   '\nХотите вийти нажмите (Q)').strip().lower()
    if choice == 'a':
        choice = 'weapoons_ak'
        new_member(choice)
    elif choice == 'п':
        choice = 'weapoons_pm'
        new_member(choice)
    elif choice == 'q':
        quit()
    else:
        print('Ввели какуюто хрень')
        user_choice()
    return choice

# user_choice()


if __name__ == '__main__':
    pass
