from datetime import datetime, timezone, timedelta
from pathlib import Path
import sqlite3


ROLL_INTERVAL = timedelta(hours=1)
CLAIM_INTERVAL = timedelta(hours=3)

SAVEFILE_PATH = Path(__file__).resolve().parent.parent/"data"/"save.db"
savefileConnection = sqlite3.connect(SAVEFILE_PATH)


def checkAndUpdateForResets():
    state = savefileConnection.execute("""
        SELECT maxRolls, rollsLeft, claimAvailable
        FROM player
    """).fetchone()

    timers = savefileConnection.execute("""
        SELECT rollResetTimestamp, claimResetTimestamp
        FROM settings
    """).fetchone()

    maxRolls, rollsLeft, claimAvailable = state
    rollResetTimestamp, claimResetTimestamp = timers

    now = datetime.now(timezone.utc)
    rollResetTimestamp = datetime.fromisoformat(rollResetTimestamp)
    claimResetTimestamp = datetime.fromisoformat(claimResetTimestamp)

    if now >= rollResetTimestamp:
        missedResets = (now - rollResetTimestamp) // ROLL_INTERVAL + 1

        rollsLeft = maxRolls
        rollResetTimestamp += missedResets * ROLL_INTERVAL

    if now >= claimResetTimestamp:
        missedResets = (now - claimResetTimestamp) // CLAIM_INTERVAL + 1

        claimAvailable = 1
        claimResetTimestamp += missedResets * CLAIM_INTERVAL

    savefileConnection.execute("""
        UPDATE player
        SET rollsLeft = ?,
            claimAvailable = ?
    """, (
        rollsLeft,
        claimAvailable
    ))

    savefileConnection.execute("""
        UPDATE settings
        SET rollResetTimestamp = ?,
            claimResetTimestamp = ?
    """, (
        rollResetTimestamp.isoformat(),
        claimResetTimestamp.isoformat()
    ))

    savefileConnection.commit()