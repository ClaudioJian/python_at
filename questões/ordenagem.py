from .Utils import *

def ordernar():
    n1 = check_input("insere um número:")
    n2 = check_input("insere um número:")

    if n2 > n1:
        print(f'{n1} , {n2}')
    else:
        print(f'{n2} , {n1}')