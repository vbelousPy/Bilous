x = int(input("Enter x: "))
if x < 0:
    print("Cannot count factorial for a negative number!")
else:
    result = 1
    i = 1
    while i <= x:
        result *= i
        i += 1
    print("x! =", result)
