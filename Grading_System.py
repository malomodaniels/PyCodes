name = input("Enter your name: ")
if name:
	score = int(input("Enter score: "))
	if score > 100:
		print(f"{name}, please enter a valid score")
	elif score >= 70: 
		print(f"{name}, your grade is A")
	elif score>=60: 
		print(f"{name}, your grade is B")
	elif score>=50: 
		print(f"{name}, your grade is C")
	elif score>=40: 
		print(f"{name}, your grade is D")
	else: print(f"Ooops! {name}, your grade is F")
else: print ("Ooops! Enter your name to proceed")

#name = input("Enter your name: ")
#if name == "Arya Stark":
#print(f"{name}, Valar Morghulis")
#elif name == "John Snow":
#	print("You know nothing")
#else:
#	print("Carry On!")