def start():
		operation = int(input("Enter; 1 for Factorial || 2 for Combination || 3 for Permutation: "))
		select(operation)

def select(operation):
		if operation == 1:
			value = int(input("\nEnter value: "))
			factorial(value)
		elif operation == 2:
			n = int(input("\nEnter n: "))
			r = int(input("\nEnter r: "))
			combination(n, r)
		elif operation == 3:
			n = int(input("\nEnter n: "))
			r = int(input("\nEnter r: "))
			permutation(n, r)
		else:
			print("\nInvalid selection")

def again(value):
	if value.lower() == "yes":
		print()
		start()
	exit

def exp(value):
	total = 1
	list = []
	while value >= 1:
		list.append(value)
		value -= 1
	for num in list:
		total *= num
	return total
				
def factorial(value):
	print("\n{}! = {}".format(value, exp(value)))
	value = input("\nPerform another operation?: ")
	again(value)

def combination(n, r):
	result = (exp(n)) / (exp(n-r) * exp(r))
	print("\nnCr = {n}! ÷ (({n} - {r})! × {r}!) = {result}".format(n = n, r = r, result = result))
	value = input("\nPerform another operation?: ")
	again(value)
	
def permutation(n, r):
	result = (exp(n)) / (exp(n-r))
	print("\nnPr = {n}! ÷ (({n} - {r})!) = {result}".format(n = n, r = r, result = result))
	value = input("\nPerform another operation?: ")
	again(value)


start()