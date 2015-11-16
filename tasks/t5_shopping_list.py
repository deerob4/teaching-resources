no_of_items = int(input("\nHello! How many items do you want to buy? "))
shopping_list = []

for x in range(1, no_of_items + 1):

	item = input("\nWhat's item #" + str(x) + "? ")
	quantity = str(input("How many " + item + " do you want to buy? "))
	to_add = quantity + " " + item
	shopping_list.append(to_add)

print("\nOkay, here's your list:\n")

for x in shopping_list:
	print(x)