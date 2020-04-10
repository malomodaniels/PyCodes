#On screen welcome message
print("Welcome to Rock Paper Scissors Game")
#Collects user input

# Player_1 = ["Rock", "Paper", "Scissors"]
# Player_2 = ["Rock", "Paper", "Scissors"]

Player_1 = input("Player 1, enter your choice: ")
Player_2 = input("Player 2, enter your choice: ")
#Conditional Statements	

if Player_1 == Player_2:
	print("It's a tie!")
elif Player_1 == "Rock":
	if Player_2 == "Paper":	
		print("Player_2 Wins")
	elif Player_2 == "Scissors":
		print("Player_1 Wins")
elif Player_1 == "Paper":
	if Player_2 == "Scissors":
		print("Player_2 Wins")
	elif Player_2 == "Rock":
		print("Player_1 Wins")
elif Player_1 == "Scissors":
	if Player_2 == "Rock":
		print("Player_2 Wins")
	elif Player_2 == "Paper":
		print("Player_1 Wins")
else: print("Oops! Something went wrong")