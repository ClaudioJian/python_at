from .Utils import *

def compras():
    print("As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12")
    quantidade_maça = check_input("Quantas maças compraria:")
    preço_maça = 1.30 if quantidade_maça < 12 else 1
    custo_maça = quantidade_maça * preço_maça
    print()
    print(f'você comprou {round(quantidade_maça)} maça(s) com total de preço {custo_maça:,.2f}R$, sendo cada um custa {preço_maça:,.2f}R$')