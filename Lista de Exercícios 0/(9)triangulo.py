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
	a = check_input("dê o primeiro valor de um triângulo: ")
	b = check_input("dê o segundo valor de um triângulo: ")
	c = (180 - a) - b
	if c<=0:
		for _ in range(0,2):
			print("???")
			print("!!!!!!!!!!!!!!!INVALID!!!!!!!!!!!!!!!!!!")
		continue
	print(f'o valor do terceiro ângulo é {c}')