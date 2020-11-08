#function declaration
def datatype(value):
	#indicates a string data type
	if type(value) == str:
		print("{} is a string\n".format(value))
	#indicates an integer data type
	elif type(value) == int:
		print("{} is an integer\n".format(value))
	#indicates a float/double data type
	elif type(value) == float:
		print("{} is a double".format(value))

#function calls with values illustrating the three data types wrt this program
datatype("soro soke")
datatype(419)
datatype(56.876544478863555)
