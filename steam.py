import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('steam_games.db')

# Создаем объект cursor для выполнения запросов
cursor = conn.cursor()

# Создаем таблицу games
cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        rating REAL,
        release_date DATE,
        summary TEXT
    )
''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()
