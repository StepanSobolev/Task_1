import sqlite3

db = sqlite3.connect('base.db')
cur = db.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS weapoons_ak(
#         name text,
#         surname text,
#         number text PRIMARY KEY,
#         subdivision text
#         )""")
#
# cur.execute("""CREATE TABLE IF NOT EXISTS weapoons_pm(
#         name text,
#         surname text,
#         number text PRIMARY KEY,
#         subdivision text
#         )""")


def new_member(table):
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    number = input('Введите номер: ').strip()
    subdivision = input('Введите подрзделение: ')
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

user_choice()



