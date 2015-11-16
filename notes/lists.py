# We use lists to store a variety of data in a single variable.
# They look just like you might imagine them to:

names = ['Augustus', 'Elizabeth', 'George', 'Maria', 'William']

# We begin a list by using [square brackets], and seperate each
# item with a comma. You can store numbers inside a list:

primes = [2, 3, 5, 7, 11]

# You can also use variables inside them:

town = "Shrewbury"
county = "Shropshire"
country = "England"

my_life = [town, county, country]

# A single list can contain a variety of data, like so:

my_list = ['Python', True, country, 10]

# To access something inside the list, we use square bracket notation.
# It looks like 'list[x]' where 'x' is the index of the item you want to
# get. Python uses zero-indexing, which means that the list starts at 0.

print(my_life[0])

# This will print out 'Shrewsbury', because the zero-th item in the list was 
# a variable with 'Shrewsbury inside'.

print(my_life[1])

# This will print out 'Shropshire', because '1' in zero-indexing corresponds to
# the second item. This is confusing at first, but you'll get the hang of it!

# Looping through a list is quite similar to the standard 'for in range()' syntax 
# you learnt before. This time, though, it's 'for in list_name'. This will print out the list
# vertically, so is more pleasant to read.

planets = ['Earth', 'Mars', 'Jupiter']

for x in planets:
	print(x)

# To add something to a list, use list_name.append(item_to_append).
# If we wanted to fill a list with the numbers 1 - 99, we could do this:

numbers = []

for x in range(0, 100):
	numbers.append(x)

# This would fill the empty 'numbers' list with 0 - 99. 
# To remove an item, use list_name.pop[x], where x is the 
# index of the item you want to remove. To remove 'Earth' from the 
# planets list, we would do:

planets.pop(x)

# You can also use list_name.remove(x), where x is the name of the
# actual ite, if you know what it is called.
