while True:
	opt = int(input())
	if(opt==0):
		break
	n = int(input("Enter a number:"))

	if n&1:
		print("odd")
	else:
		print("even")

