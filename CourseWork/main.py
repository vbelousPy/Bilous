from CourseWork.notebook_commands import *

while True:
    command = input("Enter the command (h - help): ")
    if command == "a":
        command_add()
    elif command == "s":
        command_show()
    elif command == "h":
        command_help()
    elif command == "q":
        break
    elif command == "f":
        command_find()
    else:
        print("Invalid command")