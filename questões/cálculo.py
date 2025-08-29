from .Utils import *

def múltiplo(num , multiplos):
    return "V" if num % multiplos == 0 else "F"
def positivo(num):
    return num >= 0

def calculo():
    num1 = check_input("número 1: ")
    num2 = check_input("número 2: ")

    divisão = num1 / num2
    resto = num1 % num2 if is_int(num1 , num2) else "not int"
    resultado_Q3=f' resto :{resto} divisão: {divisão if is_int(num1 ,num2) else "not int" } inteiro :{num1//num2 if is_int(num1 ,num2) else "not int"}'
    n = 12
    n1 = len('num 1: F num 2: F')
    n2 = len(resultado_Q3)
    len_Q8 = len('num 1: Ímpar num 2: Ímpar')
    
    print(f'{"|"} {" ":>15} | {"Questão 1":>{n}} | {"Questão 2":>{n}} | {"Questão 3":>{n2}} |\n{'-'*115}') #ajuste
    print(f'{"|"} {"resultado":>15} | {divisão:>{n},.2f} | {resto:>{n}} | ',end="")
    print(f'{resultado_Q3} | ')

    print("="*115)

    print(f'{"|"} {" ":>15} |{"Questão 10":>{n}} | Questão 12 \n{'-'*60}')
    print(f'{"|"} {"resultado":>15} | {num1 / num2 if num1 > num2 else num2 / num1:>{n}}',end=" | ")
    print(f'{num1 if num1 < num2 else num2}')

    print("="*115)

    print(f'{"|"} {" ":>9} | {"Questão 6":^{n1}} | {"Questão 7":^{n1}} | {"Questão 8":^{len_Q8}} | {"Questão 18":^{n1}}\n{'-'*100}')
    print(f'| divisível | {"10":^{n1}} | {"5":^{n1}} | {"2 (par ou ímpar)":^{len_Q8}} | {"9":^{n1}}\n{'-'*100}')
    print(f'{"|"} {" ":>9} |',end="")
    for multiplo in [10 ,5 ,2 ,9]:
        n1_divisível = múltiplo(num1 , multiplo)
        n2_divisível = múltiplo(num2 , multiplo)
        if multiplo == 9 :
            if is_int(num1):
                n1_divisível = "not int"
            if is_int(num2):
                n2_divisível = "not int"
        if multiplo == 2:
            Q8_num1 = "Par" if n1_divisível == "V" else "Ímpar"
            Q8_num2 = "Par" if n2_divisível == "V" else "Ímpar"
            result_Q8 = f'num 1: {Q8_num1} num 2: {Q8_num2}'
            print(f' {result_Q8:>{len_Q8}}',end=' |')
        else:
            result=f'num 1: {n1_divisível} num 2: {n2_divisível}'
            print(f' {result:^{n1}}',end=' |')

    print()
    print("="*115)

    print(f'| {" ":>14} | {"Questão 11 e Questão 14":>{n}}\n{'-'*50}')
    print(f'| {"sinal":>14} | num 1 :{"positivo" if positivo(num1) else "negativo"} num2 :{"positivo" if positivo(num1) else "negativo"}')
    print('-'*50)
    print(f'| resultado(Q14) | num 1 :{num1 /2 if positivo(num1) else num1**2} num2 :{num2 /2 if positivo(num2) else num2**2}')

    print("="*115)

    print(f'| {" ":>5} | {"Questão 15 "}\n{'-'*100}')
    print(f'| {"MAIOR"} | num 1 :{"É MAIOR QUE 10!" if num1>10 else "NÃO É MAIOR QUE 10!"} num2 :{"É MAIOR QUE 10!" if num2>10 else "NÃO É MAIOR QUE 10!"}')

    print("="*115)

    print(f'| {" ":>11} | {"Questão 21 "}\n{'-'*100}')
    print(f'| {" ":>11} | {"num 1"} | {"num 2"}\n{'-'*100}')
    print(f'| {"antecessor":>11} | {num1 - 1 if is_int(num1) else "not int"} | {num2 - 1 if is_int(num2) else "not int"}\n{'-'*100}')
    print(f'| {"sucessor":>11} | {num1 + 1 if is_int(num1) else "not int"} | {num2 + 1 if is_int(num2) else "not int"}\n{'-'*100}')

    print("="*115)