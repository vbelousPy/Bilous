n = int(input("Enter n: "))
if n <= 0:
    print("Fibonacci only for a number > 0")
else:
    if n == 1:
        print("result = 0")
    else:
        prevResult = 0
        result = 1
        i = 2
        while i < n:
            tmp = result
            result += prevResult
            prevResult = tmp
            i += 1
        print("Fibonacci series =", result)
