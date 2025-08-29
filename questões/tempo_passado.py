from .Utils import *

def Minutagem():
    Hora = check_input("insere Hora:")
    Minuto = check_input("insere Minuto:")
    if Minuto < 0 or Hora < 0:
        print("Insere número positivo!")
    elif Minuto > 60 :
        print("Minuto deve ser abaixo de 60!")
    elif Hora >= 24 :
        print("Já passou um dia")
    else:
        tempo_passado = Hora * 60 + Minuto
        print(f'Tempo passou em minuto é {tempo_passado}')