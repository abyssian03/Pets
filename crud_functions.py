import sqlite3

def initiate_db():
    connection = sqlite3.connect("for_telegram.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL)
    ''')

    # descript = ["Витаминный комплекс", "Минеральный комплекс", "Ноотропный комплекс", "Комплекс для здорового сна"]
    # for i in range(4):
    #     cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
    #                    (f'{i}', f"Product {i + 1}", f"{descript[i]}", f"{(i + 1) * 100}"))

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("for_telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, price FROM Products",)
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return(products)

def is_included(username):
    connection = sqlite3.connect("for_telegram.db")
    cursor = connection.cursor()
    user = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    connection.commit()
    if user.fetchone() is None:
        connection.close()
        return False
    else:
        connection.close()
        return True

def add_user(username, email, age):
    connection = sqlite3.connect("for_telegram.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",(f'{username}', f'{email}', f'{age}', "1000"))
    connection.commit()
    connection.close()
