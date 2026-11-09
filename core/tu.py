from core.savefile import savefileConnection, checkAndUpdateForResets
from datetime import datetime, timezone, timedelta
from math import ceil


def tu():
    checkAndUpdateForResets()

    rollsData = savefileConnection.execute("SELECT rollsLeft, claimAvailable FROM player").fetchone()
    timers = savefileConnection.execute("SELECT rollResetTimestamp, claimResetTimestamp FROM settings").fetchone()

    rollsLeft, claimAvailable = rollsData
    rollResetTimestamp, claimResetTimestamp = timers

    rollResetTimestamp = datetime.fromisoformat(rollResetTimestamp)
    claimResetTimestamp = datetime.fromisoformat(claimResetTimestamp)

    minutesTillNextRollsReset = ceil((rollResetTimestamp - datetime.now(timezone.utc)).total_seconds() / 60)

    minutesTillNextClaimReset = ceil((claimResetTimestamp - datetime.now(timezone.utc)).total_seconds() / 60)
    hoursTillNextClaimReset = minutesTillNextClaimReset // 60
    minutesTillNextClaimReset -= hoursTillNextClaimReset * 60

    tuMessage = []

    if rollsLeft == 1:
        tuMessage.append(f"You have 1 roll left. Next rolls reset in {minutesTillNextRollsReset} min.\n")

    else:
        tuMessage.append(f"You have {rollsLeft} rolls left. Next rolls reset in {minutesTillNextRollsReset} min.\n")

    if claimAvailable:
        tuMessage.append(f"You can claim right now! The next claim reset is in {hoursTillNextClaimReset}h {minutesTillNextClaimReset} min.")

    else:
        tuMessage.append(f"You can't claim for another {hoursTillNextClaimReset}h {minutesTillNextClaimReset} min.")

    tuMessage = "".join(tuMessage)

    return tuMessage