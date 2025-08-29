class end_function(Exception):
	pass
class invalid_number(Exception):
	pass

Exit = ["EXIT","EX","E"]

def check_cmd(text):
	command = input(text).strip()
	cmd = command.upper()
	print()
	if cmd in Exit:
		print("Exiting...")
		exit()
	elif cmd =="X":
		print("questão encerrada")
		raise end_function()
	elif cmd == "" :
		print("insere alguma coisa!")
		return None
	return command

def input_handler(text:str)->str:
	command = check_cmd(text)
	try:
		float(text)
		print("insere texto!")
		return input_handler(text)
	except ValueError:
		return command

def check_input(text:str)->float:
	command = check_cmd(text).strip()
	try :
		return float(command)
	except ValueError :
		print("Insere número!")
		return check_input(text)

def is_int(num1 , num2 = 1):
    return num1 % 1 == 0 and num2 % 1 == 0

def intro(text,n=15,END='\n'):
    header_main= "-" * 30 + "python atividade" + "-" * 30
    header="-" * n + text +"-" * n
    Width_intro=len(header_main)

    print("",end=END)
    print(f'{header:^{Width_intro}}')
    print("",end=END)