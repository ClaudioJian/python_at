from questões import *

#--------------------------------------------------= Dict =----------------------------------------------------------------------------------------------
questoes={
    	("1","2","3","6" ,"7" ,"8" , "10" , "11" , "12"):calculo,
	"4":idade,
	"5":bissexto,
}

#--------------------------------------------------= Main loop =----------------------------------------------------------------------------------------------
intro("python atividade",45,'')
print("escolhe um número correspodente ao questão, somente número é permitido")
print(""" 
>>> Enter "x" to back to menu in any position <<<
>>> Enter "e" to exit in any position <<<  
          
      os questões abaixo são agrupados:
	- 1 2 3 6 7 8 10 11 12
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
            print(e)

if __name__  == "__main__":
	main()