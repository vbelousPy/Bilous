n = int(input("Enter n: "))
if n <= 0:
    print("Fibonacci only for a number > 0")
else:
    resultList = [0]
    resultStr = "result = "
    if n > 1:
        resultList.append(1)
        while len(resultList) < n:
            i = len(resultList) - 1
            resultList.append(resultList[i] + resultList[i - 1])

    for i in resultList:
            resultStr += str(i) + " "
    print(resultStr)
