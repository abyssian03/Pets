import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')
for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", "1000"))

for i in range(5):
    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i*2+1}"))

for i in range(4):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i*3+1}",))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60, ))
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()