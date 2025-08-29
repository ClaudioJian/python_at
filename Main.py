from questões import *

#--------------------------------------------------= Dict =----------------------------------------------------------------------------------------------
questoes={
    ("1","2","3","6" ,"7" ,"8" , "10" , "11" , "12" ,"14" ,"15", "18","21"):calculo,
	("4" ,"20"):idade,
    "5":bissexto,
    "9":idades,
	"13":ordernar,
    ("16","19"):média,
    "17":compras,
    "22":Minutagem
}

#--------------------------------------------------= Main loop =----------------------------------------------------------------------------------------------
intro("python atividade",45,'')
print("escolhe um número correspodente ao questão, somente número é permitido")
print(""" 
>>> Enter "x" to back to menu in any position <<<
>>> Enter "e" to exit in any position <<<  
          
      os questões abaixo são agrupados:
    - 1 2 3 6 7 8 10 11 12 14 15 18 21 cálculo de múltiplos ,par ou ímpar , positivo ou negativo , comparação entre 2 números e divisão
    - 4 20 detectar se é maior que 18 (>16 pode votar) 
    - 16 e 19 média
      """)

def main():
    while True:
        try:
            intro("menu")
            option=str ( int ( (check_input("escolhe uma questão: "))))
            for questao , command in questoes.items():
                if option in questao:
                    while True:
                        intro(command.__name__,20)
                        command()
            else:
                print("questão não encontrado")
        except (Exception, end_function) as e:
            print(f'ERROR ! {e}')

if __name__  == "__main__":
	main()