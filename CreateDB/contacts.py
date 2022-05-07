import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE if not exists contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("insert into contacts(name, phone, email) values('Tim', 6545678, 'tim@email.com')")
db.execute("Insert into contacts values('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("Select * from contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit()
db.close()
