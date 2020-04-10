#On screen welcome message
print("Welcome to Rock Paper Scissors Game")
#Collects user input
Player_1 = ["Rock", "Paper", "Scissors"]
Player_2 = ["Rock", "Paper", "Scissors"]

Player_1 = input("Player 1, enter your choice: ")
Player_2 = input("Player 2, enter your choice: ")
#Conditional Statements
if Player_1 and Player_2:
	if (Player_1 == "Rock" and Player_2 == "Paper") or (Player_1 == "Paper" and Player_2 == "Scissors") or (Player_1 == "Scissors" and Player_2 == "Rock"):
		print("Player_2 Wins")
	elif Player_1 == "Scissors" and Player_2 == "Rock":
		print("Player_2 Wins")
	elif Player_1 == Player_2:
		print("Oops! It's a tie")
	else: print("Player_1 Wins")

else: print("Oops! You have to enter your choice")