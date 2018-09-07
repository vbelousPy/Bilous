text = input("Input text: ")
step = int(input("Enter step: "))
i = 0
while i < len(text):
    print(text[i::step])
    i += 1
