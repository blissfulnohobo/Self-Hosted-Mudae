import sqlite3
from pathlib import Path
from scripts.charactersList import characters


DB_PATH = Path(__file__).resolve().parent.parent/"data"/"characters.db"

def initialize():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    connection = sqlite3.connect(DB_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            series TEXT NOT NULL,
            gender TEXT NOT NULL,
            roulette TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def importCharacters():
    connection = sqlite3.connect(DB_PATH)

    connection.executemany("""
        INSERT OR IGNORE INTO characters (id, name, series, gender, roulette)
        VALUES (?, ?, ?, ?, ?)
    """, characters)

    connection.commit()
    connection.close()