import random
Player_Score = 0
Computer_Score = 0
Rounds = 3
print("Welcome to Rock Paper Scissors Game")					#On-screen welcome message

while Player_Score < Rounds and Computer_Score < Rounds:
	print(f"Current Score: {Player_Score}, {Computer_Score}")
	Player = input("Player, enter your choice: ")#.lower()			#Collects user input

	rand_num = random.randint(0,2)
	if (rand_num == 0):
	 	Computer = "Rock"
	elif (rand_num == 1):
		Computer = "Paper"
	else:
	 	Computer = "Scissors"
	print(f"Computer plays: {Computer}")

	#Conditional Statements	

	if Player == Computer:		
		print("It's a tie!")
	elif Player == "Rock":
		if Computer == "Paper":	
			print("Computer Wins")
			Computer_Score += 1
		elif Computer == "Scissors":
			print("Player Wins")
			Player_Score += 1
	elif Player == "Paper":
		if Computer == "Scissors":
			print("Computer Wins")
			Computer_Score += 1
		elif Computer == "Rock":
		 	print("Player Wins")
		 	Player_Score += 1
	elif Player == "Scissors":
		if Computer == "Rock":
			print("Computer Wins")
			Computer_Score += 1
		elif Computer == "Paper":
	 		print("Player Wins")
	 		Player_Score += 1
	else: print("Oops! Something went wrong")
print(f"Final Score: {Player_Score}, {Computer_Score}")



# if Player == Computer:
# 	print("It's a tie!")
# elif Player == "rock":
# 	if Computer == "paper":	
# 		print("Computer Wins")
# 	else:
# 		print("Player Wins")
# elif Player == "paper":
# 	if Computer == "scissors":
# 		print("Computer Wins")
# 	else:
# 		print("Player Wins")
# elif Player == "scissors":
# 	if Computer == "rock":
# 		print("Computer Wins")
# 	else:
# 		print("Player Wins")
#else: 
#	print("Oops! Wrong move")