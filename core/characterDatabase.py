import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent/"data"/"characters.db"
connection = sqlite3.connect(DB_PATH)