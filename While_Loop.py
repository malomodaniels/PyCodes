# password = input("Please enter your password: ")
# while password != "Hero":
# 	print("Password Incorrect")
# 	password = input("Please enter your password: ")
# 	print("Welcome! :) ") 
# number = 2
# while number < 10:
# 	print(number)
# 	number += 2
# for number in range(1, 10):
# 	print("\U0001f600" * number)

# number = 1
# while number < 10:
# 	print("\U0001f600" * number)
# 	number += 1

for number in range(1,10):
	count = 1
	smileys = ""
	while count < number:
		smileys += "\U0001f600"
		count += 1
	print(smileys)