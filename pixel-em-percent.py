def design():
	pixel = float(input("Enter value in pixel: "))
	em = pixel/16
	percent = (pixel*100)/16
	print("{}px = {}em = {}%".format(pixel, em, percent))
	
design()