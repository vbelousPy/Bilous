from re import match

from CourseWork.human_item import Human


def command_help():
    print("a - Add new person\n"
          "s - Show list of people\n"
          "h - Help\n"
          "q - Quit\n"
          "f - Find a person by substring")


def command_show():
    try:
        f = open("database.txt", "r+")
        print(f.read())
        f.close()
    except (FileNotFoundError, OSError, IOError):
        print("Error reading file")


def command_add():
    while True:
        first_name = input("Enter first name:")
        last_name = input("Enter last name:")
        city = input("Enter city:")
        date_birth = input("Enter date of birth in yyyy-MM-dd format:")
        if first_name and last_name and city and match("^\\d{4}-\\d{2}-\\d{2}$", date_birth):
            human = Human(first_name, last_name, city, date_birth)
            break
        else:
            print("Incorrect data")

    try:
        f = open("database.txt", "a+")
        f.write(str(human) + "\n")
        f.close()
    except (FileNotFoundError, OSError, IOError):
        print("Error writing file")


def command_find():
    substring = input("Enter substring for searching: ")
    try:
        f = open("database.txt", "r+")
        human_base = f.read().split("\n")
        for human_str in human_base:
            try:
                if human_str:
                    human = Human(*human_str.split(";"))
                    if human == substring:
                        print(human)
            except TypeError:
                print("Line error in database")
        f.close()
    except (FileNotFoundError, OSError, IOError):
        print("Error reading file")
