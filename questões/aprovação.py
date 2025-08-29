from .Utils import *

aliases_ordem = {
    1:"primeira",
    2:"segunda",
    3:"terceira",
    4:"último"
}

def média_aritmetica(notas):
    index=0
    peso_total = 0
    nota_need = 8.0
    if len(notas) == 3:
        pesos = [2,3,5]
        soma_ponderada = 0
        nota_need = 9.0
        while index < 3:
            soma_ponderada += notas[index] * pesos[index]
            peso_total += pesos[index]
            index += 1
        media = soma_ponderada / peso_total
    else:
        
        total = 0
        while index < len(notas):
            total += notas[index]
            index += 1
        media = total / len(notas)
    return media ,nota_need

def média():
    notas = []
    quantidade_prova = int(check_input("quantos provas tem: "))
    
    for n in range(1,quantidade_prova+1):
        nota_nome = aliases_ordem.get(n ,f"{n}ª")
        nota = check_input(f"insere a {nota_nome} nota :")
        notas.append(nota)

    media ,nota_necessário= média_aritmetica(notas)
    if media >= nota_necessário:
        status = "aprovado"
        nota_falta = ""
    else:
        status = "Não aprovado"
        nota_falta = f'falta {nota_necessário - media:.2f}'
    print(f'seu média é {media} e foi {status}.(mín necessário: {nota_necessário}) {nota_falta}')