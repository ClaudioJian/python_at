from .Utils import *

def idades():
    nome1 = input_handler("Digite o nome do usuário: ")
    nome2 = input_handler("Digite outro nome do usuário: ")
    idade1 = int(check_input("Digite o idade do primeiro usuário: "))
    idade2 = int(check_input("Digite o idade do segundo usuário: "))

    if idade1 % 1 != 0 or idade2 % 1 != 0:
        print("o idade não deve ser número decimal")
    elif idade1 < 0 or idade2 <0 :
        print("idade deve ser positivo!")
    else:
        print(f'user1 - {nome1} : {idade1}')
        print(f'user2 - {nome2} : {idade2}\n')
        print(f'Total: {idade1+idade2}')


