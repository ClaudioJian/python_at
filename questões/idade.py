from .Utils import *

#-------------------------------------------------- Funções auxiliares --------------------------------------------------

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_month_day(year):
    return [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

def calcular_idade_dia(data_nascimento: tuple, data_atual: tuple):
    dia_nasc, mes_nasc, ano_nasc = data_nascimento
    dia_atual, mes_atual, ano_atual = data_atual
    
    mes_max = None
    total_dias = 0
    
    # Dias dos anos completos entre nascimento e data atual
    for ano in range(ano_nasc + 1, ano_atual):
        total_dias += 366 if is_leap_year(ano) else 365

    
    dias_no_ano_nasc = get_month_day(ano_nasc)
    dias_no_ano_atual = get_month_day(ano_atual)

    if ano_atual == ano_nasc:
        mes_max = mes_atual - 1
        total_dias = dia_atual - dia_nasc if mes_atual == mes_nasc else dias_no_ano_nasc[mes_nasc - 1] - dia_nasc + dia_atual
    else:
        # Dias do ano atual até a data atual
        total_dias += dia_atual
        for dias in dias_no_ano_atual[:mes_atual - 1]:
            total_dias += dias
        total_dias += dias_no_ano_nasc[mes_nasc - 1] - dia_nasc

    # Dias restantes no ano de nascimento

    for dias in dias_no_ano_nasc[mes_nasc:mes_max]:
        total_dias += dias
    
    # Cálculo da idade em anos
    idade_anos = ano_atual - ano_nasc
    if (mes_atual, dia_atual) < (mes_nasc, dia_nasc):
        idade_anos -= 1

    # Total de dias vividos (aproximado)
    diferenca = mes_atual - mes_nasc
    idade_mes = (ano_atual - ano_nasc) * 12 + diferenca

    if dia_atual < dia_nasc:
        idade_mes -= 1

    if total_dias < 0 or ano_nasc > ano_atual:
        print("invalid")
        return None , None , None
    
    return total_dias, idade_mes , idade_anos

def validacao_data(texto):
    while True:
        data = input_handler(texto).strip()
        try:
            dia, mes, ano = [int(x) for x in data.split("/")]
            if not (1 <= mes <= 12):
                print("Mês inválido.")
                continue
            dias_mes = get_month_day(ano)
            if not (1 <= dia <= dias_mes[mes - 1]):
                print("Dia inválido.")
                continue
            return (dia, mes, ano)
        except ValueError:
            print("Formato inválido. Use dd/mm/yyyy.")

#-------------------------------------------------- Execução principal --------------------------------------------------

def idade():
    print("Use o formato dd/mm/yyyy")
    print("Idade (considerando se já passou o aniversário este ano)")
    data_nasc = validacao_data("Informe o dia, mês e ano de nascimento: ")
    data_atual = validacao_data("Informe o dia, mês e ano atual: ")

    idade_dias, idade_meses, idade_anos = calcular_idade_dia(data_nasc, data_atual)
    if idade_anos < 0 :
        print("idade inválido")
    elif idade_anos >= 18:
        print("maior de idade")
    elif idade_anos <= 18:
        print("menor de idade")
    if idade_anos <= 16 :
        print(f"Não pode votar ,falta {16 - idade_anos} anos para votar")
    else:
        print("Pode votar")
if __name__ == "__main__":
    idade()