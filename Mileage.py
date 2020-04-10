print("How many kilometers did you clock today?")
kms = input()
print("Okay, you said "+kms+"kms")
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"You covered {miles}")