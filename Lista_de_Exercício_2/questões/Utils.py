class end_function(Exception):
	pass
class invalid_number(Exception):
	pass

def check_input(text:str)->int:
	Exit = ["EXIT","EX","E"]
	command = input(text).strip()
	print()
	try :
		x=float(command)
		return x
	except ValueError :
		cmd=command.upper()
		if cmd in Exit:
			print("Exiting...")
			exit()
		elif cmd =="X":
			print("questão encerrada")
			raise end_function()
		elif cmd == "" :
			print("insere alguma coisa!")
			return check_input(text)
		else:
			print(f"digite número invéz de {cmd}")

def intro(text,n=15,END='\n'):
    header_main= "-" * 30 + "python atividade" + "-" * 30
    header="-" * n + text +"-" * n
    Width_intro=len(header_main)

    print("",end=END)
    print(f'{header:^{Width_intro}}')
    print("",end=END)