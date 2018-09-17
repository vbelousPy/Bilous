result = str()
try:
    f = open("input.txt", "r")
    fileLength = len(f.read())
    i = 0
    while i < fileLength / 2:
        f.seek(i)
        result += f.read(1)
        if not i == fileLength - (i + 1):
            f.seek(fileLength - (i + 1))
            result += f.read(1)
        i += 1
    f.close()
except (FileNotFoundError, IOError, OSError):
    print("Error")
print(result)
