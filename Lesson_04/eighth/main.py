myAlpha, myNumber, myOther = ["", "", ""]
try:
    f = open("input.txt", "r")
    temp = f.read(1)
    while temp:
        if ord("a") <= ord(temp) <= ord("z") or ord("A") <= ord(temp) <= ord("Z"):
            myAlpha += temp
        elif temp.isdigit():
            myNumber += temp
        else:
            myOther += temp
        temp = f.read(1)
    f.close()
except (FileNotFoundError, IOError, OSError):
    print("Error")

try:
    f = open("alpha.txt", "w")
    f.write(myAlpha)
    f.close()
except (FileNotFoundError, IOError, OSError):
    print("Error")
try:
    f = open("number.txt", "w")
    f.write(myNumber)
    f.close()
except (FileNotFoundError, IOError, OSError):
    print("Error")
try:
    f = open("other.txt", "w")
    f.write(myOther)
    f.close()
except (FileNotFoundError, IOError, OSError):
    print("Error")
