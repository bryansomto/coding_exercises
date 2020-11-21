import random #python random module

p1 = int(input("Enter a value from 1 - 10: ")) #get user input
p2 = (random.randint(1,10)) #random method to generate random numbers in range specified within parenthesis
if p1 not in range(1, 11): #validate user inputto be sure it's within range.'
	print("\nYour value is out of range.")
else:
	print ("\nYou selected {} || Computer selected {}".format(p1,p2))
	if p1 > p2:
		print("\nYou Win")
	elif p1 < p2:
		print("\nYou lose")
	elif p1 == p2:
		print("\nTIE")