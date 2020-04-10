import random

rand_number = random.randint(0,10)
#print(f"Random number = {rand_number}")
User_guess = None			#This enables one to use User_guess variable even though it is yet to be defined
while User_guess != rand_number:
	User_guess = int(input("Welcome, guess a number: "))	#It keeps asking user to guess while the condition is not Truthy!
	if User_guess < rand_number:
		print("You guess is too low")
	elif User_guess > rand_number:
		print("You guess is too high")
	else:
		print("You guessed right!")
		Replay = input("Do you want to keep playing? ")
		if Replay == "y":
			rand_number = random.randint(0,10)
			User_guess = None			
		elif Replay == "n":
			print("Thanks for playing")
			break 
print(f"Actual number is {rand_number}")

