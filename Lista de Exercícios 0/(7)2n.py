def check_input(text:str)->int:
	command = input(text).strip()
	Exit = ["EXIT","EX","E"]
	try :
		x=float(command)
		return x
	except ValueError :
		if command.upper().strip() in Exit:
			print("Exiting...")
			exit()
		elif command == "" :
			print("insere alguma coisa!")
		else:
			print("invalid number!!!")
		return check_input(text)
while True:
	n=check_input("n= ")
	print(2*n)