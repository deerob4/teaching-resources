# We use loops to perform a task many times.
# Each loop contains an 'iterator', a variable
# that goes up each time the loop loops. Here is the syntax:

for x in range(0, 100):
	print(x)

# The 'for' means that we are writing a 'for' loop. There are other types.
# 'x' is the iterator. Everytime the loop runs, x will be increased by 1.
# 'in range' means that the loop will run (and 'x' will iterate) between the specified range
# Because we have specified 0 - 100, the loop will run 99 times. If we did:

for x in range(0, 50):
	print(x)

# Then the loop would run 49 times. The first number is where you
# want the loop to start (it will usually be 0), and the second 
# number is one above where you want the loop to end.
# Whatever is inside the loop is what will happen each time
# the loop runs. The above loop would print out 0 - 49, because
# x is increasing by 1 each time. This, however:

for x in range(0, 51):
	print("Life just goes round and round...")

# Would print 'Life just goes round and round...' 50 times.

# Another type of loop, a 'while' loop, only functions when a condition
# is True. Consider this:

x = 0

while x < 100:
	x += 1
	print(x)

# The 'x < 10' is a conditional statement, just like the if statements from before.
# This script performs the same function as the first for loop - prints out 0 - 99.
# As you can seem we have had to declare 'x' before we can use it. In addition, we
# must iterate it ourselves, using 'x += 1'. This is the same as 'x = x + 1'.
# While loops are generally inferior, and should not be used if a for loop can accomplish 
# the same thing, which it usually can. However:

while True:
	print("I will be printed forever!")

# 'while True' will loop something forever, which can come in quite useful.
