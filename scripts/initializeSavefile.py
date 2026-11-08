import sqlite3
from pathlib import Path
from datetime import datetime, timezone, timedelta


SAVEFILE_PATH = Path(__file__).resolve().parent.parent/"data"/"save.db"

def initializeSavefile():
    SAVEFILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    connection = sqlite3.connect(SAVEFILE_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS player (
            maxRolls INTEGER NOT NULL,
            rollsLeft INTEGER NOT NULL,
            claimAvailable INTEGER NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS claimedCharacters (
            character_id INTEGER PRIMARY KEY
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            rollResetTimestamp TEXT NOT NULL,
            claimResetTimestamp TEXT NOT NULL
        )
    """)

    if connection.execute("SELECT COUNT(*) FROM player").fetchone()[0] == 0:
        connection.execute("""
            INSERT INTO player VALUES (?, ?, ?)
        """, ("10", "10", "1"))

    if connection.execute("SELECT COUNT(*) FROM settings").fetchone()[0] == 0:
        midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)

        connection.execute("""
            INSERT INTO settings VALUES (?, ?)
        """, (midnight.isoformat(), midnight.isoformat()))

    connection.commit()
    connection.close()