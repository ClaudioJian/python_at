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
	lado1=check_input("lado1: ")
	altura=check_input("altura: ")
	Area=lado1*altura
	Area_Tri=Area/2
	Perimetro_Qua=2 * lado1 + 2 * altura

	print(f'Area triangulo: {Area_Tri} ,Area Quadrado: {Area}, Perímetro do quadrado/retângulo:{Perimetro_Qua}')