import os

while True:
    print("\nIntelligent Notes Management System")
    print("1. Read & Analyze Notes")
    print("2. Create a New Note")
    print("3. Modify an Existing Note")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # -----------------------------
    # 1. Read & Analyze
    # -----------------------------
    if choice == "1":
        filename = input("Enter filename (with .txt): ")

        if os.path.exists(filename):
            file = open(filename, "r")
            content = file.read()
            file.close()

            print("\nFile Content:\n")
            print(content)
        else:
            print("File not found!")

        

    # -----------------------------
    # 2. Create Note
    # -----------------------------
    elif choice == "2":
        filename = input("Enter new filename (with .txt): ")
        file = open(filename, "w")

        print("Enter content (type END to stop):")
        while True:
            line = input()
            if line == "END":
                break
            file.write(line + "\n")

        file.close()
        print("Note created successfully!")

    # -----------------------------
    # 3. Modify Note
    # -----------------------------
    elif choice == "3":
        filename = input("Enter filename to modify: ")

        if os.path.exists(filename):
            file = open(filename, "r")
            print("\nCurrent Content:\n")
            print(file.read())
            file.close()

            file = open(filename, "w")
            print("\nEnter new content (type END to stop):")

            while True:
                line = input()
                if line == "END":
                    break
                file.write(line + "\n")

            file.close()
            print("Note modified successfully!")
        else:
            print("File not found!")

    # -----------------------------
    # 4. Exit
    # -----------------------------
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")  