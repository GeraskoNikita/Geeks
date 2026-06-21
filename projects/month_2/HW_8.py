import sqlite3

conn = sqlite3.connect("netflix.db")
cursor = conn.cursor()

# Создание таблиц
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
)
""")

# Добавляем пользователей
users = [
    ("Alex",),
    ("Bek",),
    ("Anna",),
    ("John",),
    ("Maria",)
]

cursor.executemany(
    "INSERT INTO users (name) VALUES (?)",
    users
)

# Добавляем фильмы
movies = [
    ("Inception", "Sci-Fi"),
    ("Titanic", "Drama"),
    ("Avatar", "Fantasy"),
    ("John Wick", "Action"),
    ("Interstellar", "Sci-Fi")
]

cursor.executemany(
    "INSERT INTO movies (title, genre) VALUES (?, ?)",
    movies
)

# Добавляем отзывы
reviews = [
    (1, 1, 10),
    (1, 2, 8),
    (2, 1, 9),
    (2, 3, 7),
    (3, 4, 10),
    (3, 5, 9),
    (4, 2, 6),
    (4, 3, 8),
    (5, 4, 9),
    (5, 5, 10)
]

cursor.executemany(
    "INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)",
    reviews
)

conn.commit()

# --------------------------
# ЧАСТЬ 2 — JOIN
# --------------------------

print("Имя пользователя + фильм + оценка:\n")

cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")

for row in cursor.fetchall():
    print(row)

print("\nВсе фильмы (даже без отзывов):\n")

cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews
ON movies.id = reviews.movie_id
""")

for row in cursor.fetchall():
    print(row)

# --------------------------
# ЧАСТЬ 3 — АГРЕГАЦИИ
# --------------------------

print("\nСредняя оценка:")
cursor.execute("SELECT AVG(rating) FROM reviews")
print(cursor.fetchone()[0])

print("\nМаксимальная оценка:")
cursor.execute("SELECT MAX(rating) FROM reviews")
print(cursor.fetchone()[0])

print("\nМинимальная оценка:")
cursor.execute("SELECT MIN(rating) FROM reviews")
print(cursor.fetchone()[0])

conn.close()