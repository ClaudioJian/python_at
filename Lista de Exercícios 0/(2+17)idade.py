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


ano_nasc = check_input("ano de nascimento: ")

ano_atual = check_input("ano atual: ")

idade = ano_atual - ano_nasc

print(idade)