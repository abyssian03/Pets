import sqlite3

connection = sqlite3.connect("not_telegram2.db")
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

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60, ))
#users = cursor.fetchall()
#for user in users:
#    print(user)

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(all_balances / total_users)

connection.commit()
connection.close()