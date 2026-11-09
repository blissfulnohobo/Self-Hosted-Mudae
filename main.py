import scripts.initializeCharacterDatabase
import scripts.initializeSavefile
import core.characterRolling
import core.tu


def main():
    print("Performing initial setup...")

    scripts.initializeCharacterDatabase.initialize()
    scripts.initializeCharacterDatabase.importCharacters()
    scripts.initializeSavefile.initializeSavefile()

    print("Initial setup complete!")

    print("Type $help to get started.")

    while True:
        command = input("> ").strip()

        if command == "$w" or command == "$wx":
            print(core.characterRolling.waifuRoll())

        if command == "$tu":
            print(core.tu.tu())

        elif command == "$help":
            print("Available commands:\n$w or $wx\n$tu\n$help\n$exit or $quit")

        if command == "$exit" or command == "$quit":
            break


if __name__ == "__main__":
    main()