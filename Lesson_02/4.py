i = 0
words = {}
while i < 3:
    key = input("Enter word: ")
    value = words.get(key)
    if value is None:
        value = 1
    else:
        value += 1
    words.update({key: value})
    i += 1

print("Statistics:")
for key, value in words.items():
    print(key, "-", value)
