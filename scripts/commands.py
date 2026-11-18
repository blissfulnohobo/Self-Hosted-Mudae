import core.characterRolling
import core.claiming
import core.tu
import sys
import textwrap


def parseCommand():
    fullCommand = input("> ").strip().lower().split()
            
    mainCommand = fullCommand[0]
    args = fullCommand[1:]

    if mainCommand in commands:
        commands[mainCommand](args)


commands = {
    # Roll commands
    "$wa": lambda args: print(core.characterRolling.characterRoll("waifu", "animanga")),
    "$wg": lambda args: print(core.characterRolling.characterRoll("waifu", "game")),
    "$wx": lambda args: print(core.characterRolling.characterRoll("waifu", None)),
    
    "$ha": lambda args: print(core.characterRolling.characterRoll("husbando", "animanga")),
    "$hg": lambda args: print(core.characterRolling.characterRoll("husbando", "game")),
    "$hx": lambda args: print(core.characterRolling.characterRoll("husbando", None)),

    "$ma": lambda args: print(core.characterRolling.characterRoll(None, "animanga")),
    "$mg": lambda args: print(core.characterRolling.characterRoll(None, "game")),
    "$mx": lambda args: print(core.characterRolling.characterRoll(None, None)),

    "$claim": lambda args: print(core.claiming.claimCharacter(args[0])),

    "$tu": lambda args: print(core.tu.tu()),

    "$help": lambda args: print(helpMessage),

    "$exit": lambda args: sys.exit(),
    "$quit": lambda args: sys.exit()
}

helpMessage = textwrap.dedent("""
    Available commands:
        Character Roulette:
            $wa, $wg, and $wx
            $ha, $hg, and $hx
            $ma, $mg, and $mx

        $claim [Character ID]
        $tu
        $help
        $exit or $quit
""").strip()


# Command aliases
commands["$waifu"] = commands["$wx"]
commands["$waifua"] = commands["$wa"]
commands["$waifug"] = commands["$wg"]

commands["$husbando"] = commands["$hx"]
commands["$husbandoa"] = commands["$ha"]
commands["$husbandog"] = commands["$hg"]

commands["$marry"] = commands["$mx"]
commands["$marrya"] = commands["$ma"]
commands["$marryg"] = commands["$mg"]

commands["$w"] = commands["$wx"]
commands["$h"] = commands["$hx"]
commands["$m"] = commands["$mx"]