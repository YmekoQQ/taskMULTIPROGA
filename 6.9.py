import csv
import sqlite3
# створення бази даних та таблиці ratings
conn = sqlite3.connect("imdb.db")
c = conn.cursor()
c.execute("""CREATE TABLE ratings
    (id INTEGER PRIMARY KEY, title VARCHAR(20), year INT, rating FLOAT)""")

# додавання записів з csv-файлу в таблицю ratings
with open("imdb.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) # пропускаємо перший рядок (шапку таблиці) for row in reader:
    for row in reader:
        c.execute("INSERT INTO ratings (title, year, rating) VALUES (?, ?, ?)", [row[0], row[1], row[2]])

# виведення усіх записів таблиці ratings в алфавітному порядку за полем title
c.execute("SELECT * FROM ratings ORDER BY title ASC")
for row in c.fetchall():
    print(row)

# виведення записів таблиці ratings з рейтингом більшим за 8.70 c.execute("SELECT * FROM ratings WHERE rating > 8.70")
c.execute("SELECT * FROM ratings WHERE rating > 8.70")
for row in c.fetchall():
    print(row)

# закриття з'єднання з базою даних conn.close()
conn.close()