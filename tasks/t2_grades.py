mark = int(input("\nWhat mark did you get? "))

if(mark >= 90):
	print('You got an A* - you\'re amazing!')
	print('You were ' + str(100 - mark) + ' marks away from full marks.\n')

elif(mark >= 80):
	print('You got an A - that\'s great!')
	print('You were ' + str(90 - mark) + " marks away from the next grade, an A*.\n")

elif(mark >= 70):
	print('You got a B - not bad!')
	print('You were ' + str(80 - mark) + " marks away from the next grade, and A.\n")

elif(mark >= 60):
	print('You got a C - keep going!')
	print('You were ' + str(70 - mark) + " marks away from the next grade, a B.\n")

elif(mark >= 50):
	print('You got a D - try revising a bit more.')
	print('You were ' + str(60 - mark) + " marks away from the next grade, a C.\n")

elif(mark >= 40):
	print('You got a E - you need to work a little harder.')
	print('You were ' + str(50 - mark) + " marks away from the next grade, a D.\n")

elif(mark >= 30):
	print('You got a F - perhaps some extra tuition is needed?')
	print('You were ' + str(40 - mark) + " marks away from the next grade, an E.\n")

elif(mark >= 20):
	print('You got a G - maybe you\'re not cut out for this subject?')
	print('You were ' + str(30 - mark) + " marks away from the next grade, an F.\n")

else:
	print('You got a U, I\'m afraid. See me afterwards.')
	print('You were ' + str(20 - mark) + " marks away from the next grade, a G.\n")