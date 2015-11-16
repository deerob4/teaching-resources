#Creates a loop
for x in range(0, 76):

	#Checks if x is divisible by 3 and 5
	if(x % 3 == 0 and x % 5 == 0):
		print("FizzBuzz")

	#Checks if x is divisible by 3
	elif(x % 3 == 0):
		print("Fizz")

	#Checks if x is divisible by 5
	elif(x % 5 == 0):
		print("Buzz")

	#If none of these criteria are met, just prints the number (x)
	else:
		print(x)