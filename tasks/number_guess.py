import random
import matplotlib.pyplot as plt

def guess_number(random_number):

	total = 0
	guesses = []

	while True:

		try:
			guess = int(input("\nYour guess: "))

			if(guess < random_number):
				print("You're too low!")
				guesses.append(guess)
				total += 1

			elif(guess > random_number):
				print("You're too high!")
				guesses.append(guess)
				total += 1

			else:
				guesses.append(guess)
				print("\nYou got it right - well done!")
				print("It took you", str(total), "guesses to get it!")
				plot_graph(guesses)
				break

		except ValueError:
			print("That is not a number!")

def plot_graph(array):

	plt.plot(array, array, 'ro')
	plt.axis([0, random_range, 0, random_range])
	plt.show()

random_range = random.randint(25, 300)
random_number = random.randint(1, random_range)

print("\nNumber Guessing Game")
print("-" * len("Number Guessing Game"))
print("I have chosen a number between 1 and", str(random_range) + ". Try and guess it!")

guess_number(random_number)