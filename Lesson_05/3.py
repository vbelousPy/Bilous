def foo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return foo(n - 1) + foo(n - 2)


try:
    print("result =", foo(int(input("Enter a number greater than zero: "))))
except (RecursionError, ValueError):
    print("Incorrect value")
