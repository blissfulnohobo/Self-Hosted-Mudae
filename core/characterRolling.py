from core.savefile import savefileConnection, checkAndUpdateForResets
from core.characterDatabase import characterDatabaseConnection
from datetime import datetime, timezone, timedelta
from math import ceil


def waifuRoll():
    checkAndUpdateForResets()

    rollsData = savefileConnection.execute("SELECT maxRolls, rollsLeft FROM player").fetchone()
    maxRolls, rollsLeft = rollsData

    if rollsLeft > 0:
        rolledChar = characterDatabaseConnection.execute("""
            SELECT * FROM characters
            WHERE gender = ?
            ORDER BY RANDOM()
            LIMIT 1
        """, ("waifu",)).fetchone()

        savefileConnection.execute("UPDATE player SET rollsLeft = rollsLeft - 1")

        savefileConnection.commit()

        return rolledChar

    else:
        rollResetTimestamp = savefileConnection.execute("SELECT rollResetTimestamp FROM settings").fetchone()[0]
        rollResetTimestamp = datetime.fromisoformat(rollResetTimestamp)

        minutesTillNextRollsReset = ceil((rollResetTimestamp - datetime.now(timezone.utc)).total_seconds() / 60)

        return f"The roulette is limited to {maxRolls} uses per hour. {minutesTillNextRollsReset} min left."