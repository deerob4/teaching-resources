for x in range(99, 1, -1):#

	print(str(x) + " green bottles, standing on the wall,")
	print("If one green bottle should accidentally fall,")
	print("There'll be " + str(x - 1) + " green bottles standing on the wall.\n")

	if(x < 3):
		print("Only one green bottle, standing on the wall!\n")