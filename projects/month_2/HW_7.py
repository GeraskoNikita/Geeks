import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")
conn.commit()


# CREATE
def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()


# READ
def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    for product in products:
        print(product)


# UPDATE
def update_product(product_id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, product_id)
    )
    conn.commit()


# DELETE
def delete_product(product_id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )
    conn.commit()


# Пример использования
create_product("Молоко", 85, 10)
create_product("Хлеб", 35, 20)

print("Все товары:")
read_products()

update_product(1, 90)

print("\nПосле обновления:")
read_products()

delete_product(2)

print("\nПосле удаления:")
read_products()

conn.close()