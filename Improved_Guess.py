import random

rand_number = random.randint(1,10)
#print(rand_number)
Guess = None
while Guess != rand_number:
	Guess = int(input("Guess a number between 1 and 10: "))
	if Guess == rand_number:
		print("Correct!")
		Replay = input("Do you want to continue? ")
		if Replay == "y":
			rand_number = random.randint(1,10)
			Guess = None
			#Guess = int(input("Guess a number between 1 and 10: "))	
		else:
			print("Thanks for playing")
			break
	elif Guess < rand_number:
		print("Guess too low")
	else:
		print("Guess too high")


	#else: (Guess > 10) or (Guess < 1):
	#	print("Ooops! Out of range")