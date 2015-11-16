from statistics import mode, median, mean
import random

def roll_dice(sides, times):

	numbers = []

	for x in range(1, times + 1):
		numbers.append(random.randint(1, sides))

	print("\n" + str(numbers) + "\n")

	for x in range(1, sides + 1):

		if(numbers.count(x) == 1):
			print(str(x) + " was thrown " + str(numbers.count(x)) + " time.")

		else:
			print(str(x) + " was thrown " + str(numbers.count(x)) + " times.")

	print("\nThe most common number was " + str(mode(numbers)) + ".")
	print("The median number was " + str(median(numbers)) + ".")
	print("The mean number was " + str(mean(numbers)) + ".\n")

def input_data():

	while True:

		try:
			sides = int(input("How many sides does the dice have? "))
			times = int(input("How many times should the dice be rolled? "))
			roll_dice(sides, times)
			break
			
		except ValueError:
			print("Please enter a valid integer.")

print("\nDice Rolling Program")
print("-" * len("Dice Rolling Program"))

input_data()