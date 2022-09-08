import sqlite3

db = sqlite3.connect('base.db')
cur = db.cursor()


def test(number):
    number_num = None
    if number.isdigit() == True:
        number_num = True
    if con.execute('SELECT UnitPrice FROM invoice_items').fetchall():
        return False


# print(test('5'))

print(True + True)
