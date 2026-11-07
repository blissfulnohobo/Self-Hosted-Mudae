import scripts.initializeCharacterDatabase
import core.characterRolling


def main():
    print("Performing initial setup...")

    scripts.initializeCharacterDatabase.initialize()
    scripts.initializeCharacterDatabase.importCharacters()

    print("Initial setup complete!")

    print("Type $help for available commands.")

    while True:
        command = input("> ").strip()

        if command == "$w" or command == "$wx":
            print(core.characterRolling.waifuRoll())

        elif command == "$help":
            print("Available commands:\n$w or $wx\n$help\n$exit")

        if command == "$exit":
            break


if __name__ == "__main__":
    main()