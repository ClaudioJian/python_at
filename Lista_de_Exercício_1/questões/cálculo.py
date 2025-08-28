from .Utils import *

def múltiplo5(num):
    return


def calculo():
    num1 = check_input("número 1: ")
    num2 = check_input("número 2: ")

    n=12
    n1 = 25
    print(f'{"|"} {" ":>15} | {"Questão 1":>{n}} | {"Questão 2":>{n}} | {"Questão 3":>{n}}  \n{'-'*70}')
    print(f'{"|"} {"resultado":>15} | {num1/num2:>{n},.0f} | {num1%num2:>{n},.0f} | ',end="")
    print(f' resto :{num1 %num2} divisão: {num1/num2} inteiro :{num1//num2}\n')

    print(f'{"|"} {" ":>18} | {"Questão 6":>{n1}} | {"Questão 7":>{n1}} \n{'-'*100}')
    print(f'{"|"} {"divisível por 10":>18} | num 1: {True if num1 % 10 == 0 else False} num 2 :{True if num1 % 10 == 0 else False} | num 1: {True if num1 % 5 == 0 else False} num 2 :{True if num1 % 5 == 0 else False} | num 1: {"Par" if num1 % 2 == 0 else "Ímpar"} num 2 :{"Par" if num1 % 2 == 0 else "Ímpar"} |')
    return num1,num2
