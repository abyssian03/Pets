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
