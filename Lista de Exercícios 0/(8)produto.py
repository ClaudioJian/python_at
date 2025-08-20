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
	produto=check_input("preço do produto:$ ")
	disconto=produto * 0.9
	print(f'produto com desconto:       ${disconto}')