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

def calcular_segundo_grau(a,b,c)->int:
	delta=(b**2) - (4*a*c)
	print(f'\n delta: {delta}')
	if delta < 0:
		return None ,None
	x1= (-b + (delta**(1/2)))/(2*a)
	x2= (-b - (delta**(1/2)))/(2*a)
	return x1, x2

def sinal(valor:int):
	return "+" if valor>=0 else "-"

def main():
	print(f'{"-"*10}calculador de segundo grau{"-"*10}\n')

	while True:
		a = check_input("insere uma a:")
		if a == 0:
			print("não é equação de segundo grau")
			continue
		b=check_input("insere uma b:")
		c=check_input("insere uma c:")
		x1, x2 = calcular_segundo_grau(a,b,c)    #raizes do equação
		sinal_b, sinal_c = sinal(b) ,sinal(c)    #retorna sinal do b e c para exibição do equação

		print(f'equação:{a}x^2{sinal_b}{abs(b)}x{sinal_c}{abs(c)}')
		if not x1 or not x2:
			print("não existe raíz real \n ")
			continue
		print(f'os dois raízes do equação é {x1} e {x2} \n ')


if __name__  == "__main__":
	main()