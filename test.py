import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('Inventory.db')
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''CREATE TABLE IF NOT EXISTS Inventory (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, counts INTEGER NOT NULL)''')

# Функция для получения текущего значения counts по имени
def get_count(name):
    cursor.execute("SELECT counts FROM Inventory WHERE name = ?", (name,))
    result = cursor.fetchone()
    return result[0] if result else None

# Функция для обновления значения counts по имени
def update_count(name, new_count):
    cursor.execute("SELECT id FROM Inventory WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        cursor.execute("UPDATE Inventory SET counts = ? WHERE name = ?", (new_count, name))
    else:
        cursor.execute("INSERT INTO Inventory (name, counts) VALUES (?, ?)", (name, new_count))
    conn.commit()

# Обновляем значение counts для Wood
#update_count('Wood', 10)

# Получаем обновленное значение для Wood
#updated_count_wood = get_count('Wood')
#print(f"Updated counts for Wood: {updated_count_wood}")

# Получаем данные из таблицы
cursor.execute("SELECT * FROM Inventory")
rows = cursor.fetchall()

# Выводим данные
for row in rows:
    print(row)

# Закрываем соединение с базой данных
conn.close()