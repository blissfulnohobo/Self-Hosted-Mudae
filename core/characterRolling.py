from core.savefile import savefileConnection, checkAndUpdateForResets
from core.characterDatabase import characterDatabaseConnection
from core.tu import calculateNextResets


def characterRoll(gender, roulette):
    checkAndUpdateForResets()

    rollsData = savefileConnection.execute("SELECT maxRolls, rollsLeft FROM player").fetchone()
    maxRolls, rollsLeft = rollsData

    if rollsLeft > 0:
        rolledChar = characterDatabaseConnection.execute("""
            SELECT id 
            FROM characters
            WHERE (? IS NULL OR gender = ? OR gender = 'both')
            AND (? IS NULL OR roulette = ? OR roulette = 'both')
            ORDER BY RANDOM()
            LIMIT 1
        """, (gender, gender, roulette, roulette)).fetchone()[0]

        savefileConnection.execute("UPDATE player SET rollsLeft = rollsLeft - 1")
        savefileConnection.execute("INSERT INTO rollHistory (characterId) VALUES (?)", (rolledChar,))

        # Limit rolls logged to the past 50 rolls
        savefileConnection.execute("""
            DELETE FROM rollHistory
            WHERE rollIndex NOT IN (
                SELECT rollIndex
                FROM rollHistory
                ORDER BY rollIndex DESC
                LIMIT 50
            )
        """)

        savefileConnection.commit()

        return rolledChar

    else:
        minutesTillNextRollReset = calculateNextResets()[0]

        return f"The roulette is limited to {maxRolls} uses per hour. {minutesTillNextRollReset} min left."