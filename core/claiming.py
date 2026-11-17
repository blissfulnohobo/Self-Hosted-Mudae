from core.savefile import savefileConnection, checkAndUpdateForResets
from core.characterDatabase import characterDatabaseConnection
from core.tu import calculateNextResets


def claimCharacter(characterId):
    checkAndUpdateForResets()

    claimAvailable = savefileConnection.execute("SELECT claimAvailable FROM player").fetchone()[0]
    
    wasRecentlyRolled = savefileConnection.execute(
        "SELECT EXISTS (SELECT 1 FROM rollHistory WHERE characterId = ?)",
        (characterId,)).fetchone()[0]

    alreadyClaimed = savefileConnection.execute(
        "SELECT EXISTS (SELECT 1 FROM claimedCharacters WHERE characterId = ?)",
        (characterId,)).fetchone()[0]

    characterName = characterDatabaseConnection.execute(
        "SELECT name FROM characters WHERE id = ?",
        (characterId,)).fetchone()

    if characterName is not None:
        characterName = characterName[0]

    if wasRecentlyRolled and not alreadyClaimed:
        if claimAvailable:
            savefileConnection.execute("INSERT INTO claimedCharacters (characterId) VALUES (?)", (characterId,))
            savefileConnection.execute("UPDATE player SET claimAvailable = 0")

            rollIndex = savefileConnection.execute("""
                SELECT rollIndex
                FROM rollHistory
                WHERE characterId = ?
                ORDER BY rollIndex ASC
            """, (characterId,)).fetchone()[0]

            savefileConnection.execute(
                "DELETE FROM rollHistory WHERE rollIndex = ?",
                (rollIndex,))

            savefileConnection.commit()

            print(f"💖 You and {characterName} are now married! 💖")

        else:
            hoursTillNextClaimReset = calculateNextResets()[1]
            minutesTillNextClaimReset = calculateNextResets()[2]

            if hoursTillNextClaimReset > 0:
                print(f"You can claim once per interval of 3h. The next interval begins in {hoursTillNextClaimReset}h {minutesTillNextClaimReset} min.")

            else:
                print(f"You can claim once per interval of 3h. The next interval begins in {minutesTillNextClaimReset} min.")