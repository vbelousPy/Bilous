myList = list()
while True:
    try:
        n = input("Input number: ")
        if len(n) == 0:
            break
        myList.append(float(n))
    except ValueError:
        print("Invalid value")
print(myList)
