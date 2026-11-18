import scripts.initializeCharacterDatabase
import scripts.initializeSavefile
import scripts.commands


def main():
    print("Performing initial setup...")

    scripts.initializeCharacterDatabase.initialize()
    scripts.initializeCharacterDatabase.importCharacters()
    scripts.initializeSavefile.initializeSavefile()

    print("Initial setup complete!")

    print("Type $help to get started.")

    while True:
        scripts.commands.parseCommand()

if __name__ == "__main__":
    main()