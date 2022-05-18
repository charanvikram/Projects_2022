while True:
	opt = int(input("press-0 to exit or press any number to continue"))
	if(opt==0):
		break
	n = int(input("Enter a number:"))

	if n&1:
		print("odd")
	else:
		print("even")

