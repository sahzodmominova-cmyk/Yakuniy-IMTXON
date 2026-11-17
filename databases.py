import sqlite3

db = sqlite3.connect("Menning_kitoblarin.db")
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Kitoblar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nomi VARCHAR(100),
        muallif VARCHAR(100),
        kategoriya VARCHAR(100),
        narx REAL,
        sana DATE
    )
""")

db.commit()