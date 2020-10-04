from random import *

executa = True

adjetivos = [ "maravilhoso" ,  "acima da média" ,  "excelente" ]
hobbies = [ "andar de bicicleta" , "programar" , "fezer chá"]

print("Gerador de Cumprimentos")
print("-----------------------")

nome = input("Qual é o seu nome?:")

print('''
MENU
    c = obter cumprimento
    q = sair
''')

while executa == True:

    menuChoice = input("\n>..").lower()

    if menuChoice == 'c':


        print("Aqui está o seu cumprimento" ,  nome , ":")

        print( nome , "você é" , choice(adjetivos) , "emm" , choice(hobbies))
        print( "De nada!")

    elif menuChoice == 'q':


            executa = False

    else:
            print("Escolha uma opção válida")
            
