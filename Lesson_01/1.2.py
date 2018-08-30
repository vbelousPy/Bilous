firstName = input("input first name: ")
lastName = input("input last name: ")
age = int(input("input your age: "))
man = input("Are you a man (y/n)? ") == "y"
maleBase = {True: "(man)", False: "(woman)"}
print("Hello,", firstName, lastName, ", age:", age, maleBase[man])