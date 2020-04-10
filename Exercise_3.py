#Program combining for loop and conditional logic
# for number in range(1, 21):
	
# 	if number == 4 or number == 13:
# 		print(f"{number} is unlucky")
# 	# elif number == 13:				line of execution combined already in line 5
# 	# 	print(f"{number} is unlucky")
# 	elif number % 2 == 0:
# 		print(f"{number} is even")
# 	else:
# 			print(f"{number} is odd")
	#else:
		#print(number)					no need as line has been taken care of in line 10


#########################################	shorter and more succint version of code
for number in range(1, 21):	
	if number == 4 or number == 13:
		status = "unlucky"
	elif number % 2 == 0:
		status = "even"
	else:
		status = "odd"	
	print(f"{number} is {status}")