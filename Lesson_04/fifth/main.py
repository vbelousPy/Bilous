myDict = {"beer": "пиво", "poison": "отрава"}
while True:
    key = input("Enter the word: ")
    if key == "":
        break
    value = myDict.get(key)
    if value is None:
        value = input("Word not found, enter translation: ")
        myDict.update({key: value})
    else:
        print("Translation: " + value)
print(myDict)
