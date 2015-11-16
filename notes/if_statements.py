# If statements allow your program to change depending
# on actions the user has taken. The syntax is very simple:

if(condition):
	# do something

# Inside the condition section, place a logical test
# something like 100 < 200. This equates to True, and 
# so the condition will run. This block will run:

if(100 < 200):
	print("100 is less than 200!")

# The following block will not run, because the condition
# equates to False:

if(100 > 200):
	print("100 is greater than 200!")

# Variables can also be used in conditional statements:

name = "Toby"
if(len(name) > 5):
	print("The length of 'Toby' is greater than 5!")

# The following conditions can be used in conditional statements:
# < LESS THAN 
# > GREATER THAN
# <= LESS THAN OR EQUAL TO
# >= GREATER THAN OR EQUAL TO
# == EQUAL TO
# AND
# NOT 
# OR
# They can all be combined:

if(10 < 20 and name == "Toby" or 70 <= 70 and 7 * 7 == 49):
	print("This will be printed out!")

# Because all of the statements equate to True, the statement will
# be printed out. If statements can contain multiple conditions. If the
# first is not met, it will go through until it finds one that is. Consider:

location = "Shrewsbury"

if(location == "Stafford"):
	print("I live in Stafford!")

elif(location == "Shrewsbury"):
	print("I live in Shrewsbury!")

# As 'location' was set to 'Shrewsbury', the second statement was used. If it had
# been Stafford, the first would have been used. To end an if statement, use an else block:

location = "Cardiff"

if(location == "Stafford"):
	print("I live in Stafford!")

elif(location == "Shrewsbury"):
	print("I live in Shrewsbury!")

else:
	print("I don't live in Shrewsbury or Stafford!")

# None of the explicitly mentioned conditions were met, so the else condition is used. 