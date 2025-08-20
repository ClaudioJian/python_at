def check_input(text:str)->int:
	command = input(text)
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


a= check_input("escolha um número para somar com mais 2, sendo esse A: ")
b= check_input("escolha um número para somar com mais 2, sendo esse B: ")
c= check_input("escolha um número para somar com mais 2, sendo esse C: ")

valor_total = a + b + c

print(valor_total)