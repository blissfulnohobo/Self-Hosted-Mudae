import scripts.initializeCharacterDatabase
import scripts.initializeSavefile
import core.tu
import core.characterRolling
import core.claiming


def main():
    print("Performing initial setup...")

    scripts.initializeCharacterDatabase.initialize()
    scripts.initializeCharacterDatabase.importCharacters()
    scripts.initializeSavefile.initializeSavefile()

    print("Initial setup complete!")

    print("Type $help to get started.")

    while True:
        fullCommand = input("> ").strip().lower().split()
        
        mainCommand = fullCommand[0]
        arguments = fullCommand[1:]

        if mainCommand == "$tu":
            print(core.tu.tu())

        if mainCommand == "$w" or mainCommand == "$wx":
            print(core.characterRolling.waifuRoll())

        if mainCommand == "$claim" and len(arguments):
            core.claiming.claimCharacter(int(arguments[0]))

        elif mainCommand == "$help":
            print("Available commands:\n$w or $wx\n$claim [Character ID]\n$tu\n$help\n$exit or $quit")

        if mainCommand == "$exit" or mainCommand == "$quit":
            break


if __name__ == "__main__":
    main()