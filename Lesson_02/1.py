import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b ** 2 - 4 * a * c
if d < 0:
    print("The result is a complex value")
else:
    if d == 0:
        print("x =", (-b / 2 * a))
    else:
        print("x1 =", (-b - math.sqrt(d)) / 2 * a)
        print("x2 =", (-b + math.sqrt(d)) / 2 * a)
