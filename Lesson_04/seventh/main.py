myList = [1, 2, 3, [4, 5], 6, [7]]
s = str(myList).replace("[", "").replace("]", "")
myList = s.split(", ")

try:
    f = open("myFile.txt", "w")
    f.writelines([i + "\n" for i in myList])
    f.close()
except (FileNotFoundError, IOError, OSError):
    print("Error")
