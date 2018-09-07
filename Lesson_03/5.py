length = int(input("Enter length: "))
t = int(input("Select type (1-4): "))
result = str()

if t == 1:
    i = 0
    while i < length:
        temp = "".ljust(length - i, "*")
        temp = temp.ljust(length, " ")
        result += temp + "\n"
        i += 1
elif t == 2:
    i = length - 1
    while i >= 0:
        temp = "".ljust(length - i, "*")
        temp = temp.ljust(length, " ")
        result += temp + "\n"
        i -= 1
elif t == 3:
    i = 1
    while i <= length:
        temp = "".ljust(length - i, " ")
        temp = temp.ljust(length, "*")
        result += temp + "\n"
        i += 1
elif t == 4:
    i = length
    while i >= 0:
        temp = "".ljust(length - i, " ")
        temp = temp.ljust(length, "*")
        result += temp + "\n"
        i -= 1

print(result)
