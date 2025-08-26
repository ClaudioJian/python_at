from .Utils import *

def calculo():
    num1 = check_input("número 1: ")
    num2 = check_input("número 2: ")

    n=12
    print(f'{"|"} {" ":>15} | {"Questão 1":>{n}} | {"Questão 2":>{n}} | {"Questão 3":>{n}}  \n{'-'*70}')
    print(f'{"|"} {"resultado":>15} | {num1/num2:>{n},.0f} | {num1%num2:>{n},.0f} | ',end="")
    print(f' resto :{num1 %num2} divisão: {num1/num2} inteiro :{num1//num2}\n')

    print(f'{"|"} {" ":>18} | {"Questão 6":>{n}} \n{'-'*50}')
    print(f'{"|"} {"divisível por 10":>18} | num 1: {True if num1 % 10 == 0 else False} num 2 :{True if num1 % 10 == 0 else False}')
    return num1,num2
