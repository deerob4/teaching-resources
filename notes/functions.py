# We use functions to organise our programs into sections, to
# make them easier to read. They look like this:

def function_name():
	print('I\'m inside a function!')

# You use 'def' to start a function. You follow this with 
# the function name, and then brackets, which can hold 
# variables. A colon is then used to denote the start of the 
# function. Now, everytime we want to print 'I\'m inside a function!',
# we can just do:

function_name()

# This calls the function, and runs everything inside it. One very important thing to 
# remember is that variables created inside a function cannot be used outside the 
# function. Consider this:

def say_hello():

	name = input("What is your name? ")

print("Hello there", name)

# This will result in an error, because the 'name' variable does not
# exist outside of the say_hello() function. If you were to do this:

def say_hello():

	name = "Dee"
	print("Hello there", name)

say_hello()

# The script would run correctly, because 'name' is not being referenced 
# outside the function. There are ways to get around this - if you declare a variable
# outside of all functions, it can be used anywhere:

def say_hello():
	
	print("Hello there", name)

name = "Dee"
say_hello()