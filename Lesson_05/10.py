def myrange(*args, stop=0, start=0, step=1):
    if len(args) == 1:
        if stop == 0:
            stop = args[0]
        else:
            start = args[0]
    elif len(args) > 1:
        start = args[0]
        stop = args[1]
        if len(args) > 2:
            step = args[2]

    result = list()
    while start < stop:
        result.append(start)
        start += step

    if len(result) == 0:
        print("argument error")
        return
    return result


print(myrange(100))
print(myrange(1, 100))
print(myrange(start=1, stop=100))
print(myrange(4, 100, 2))
print(myrange(start=4, stop=100, step=2))
print(myrange(4, 100, step=2))
print(myrange(4, stop=100, step=2))

print(myrange(4, start=10))
