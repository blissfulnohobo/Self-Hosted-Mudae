import sqlite3
from pathlib import Path


CHAR_DB_PATH = Path(__file__).resolve().parent.parent/"data"/"characters.db"
characterDatabaseConnection = sqlite3.connect(CHAR_DB_PATH)