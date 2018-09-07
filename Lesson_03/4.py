n = int(input("Enter number: "))
d = dict()
key = 1
while key <= n:
    value = {2: key ** 2, 3: key ** 3, 4: key ** 4}
    d.update({key: value})
    key += 1
print(d)
