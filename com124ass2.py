#array initialised
week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#function declaration
def weekdays():
	#local variable (counter) initialised
	counter = 0
	#iterate through array, increment counter by 1 and print result in each iteration
	for days in week_days:
		counter += 1
		print("Day {} of the week is {}".format(counter, days))
	return 0

#function call
weekdays()
	
	