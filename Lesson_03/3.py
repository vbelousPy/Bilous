cortege = tuple()
while True:
    text = input("Input text: ")
    if len(text) == 0:
        break
    else:
        cortege = cortege + (text,)
print(cortege)
