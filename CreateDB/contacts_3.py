import sqlite3

db = sqlite3.connect("contacts.sqlite")

name_1 = input("Please enter a name to be searched:")

# for row in db.execute(f"select * from contacts where name = ?", (name_1,)):
for row in db.execute(f"select * from contacts where name like ?", (name_1,)):
    print(row)

db.close()
