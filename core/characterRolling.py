from core.characterDatabase import connection


def waifuRoll():
    rolledChar = connection.execute("""
        SELECT * FROM characters
        WHERE gender = ?
        ORDER BY RANDOM()
        LIMIT 1
    """, ("waifu",)).fetchone()

    return rolledChar