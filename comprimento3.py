from random import *

executa = True

adjetivos = [ "maravilhoso" ,  "legal" ,  "bonito" ]
hobbies = [ "correr" , "brincar" , "jogar"]

print("Gerador de Cumprimentos")
print("-----------------------")

nome = input("Qual o nome do seu animal de estimação:")

print('''
MENU
    c = obter cumprimento
    a = adicionar hobby
    d = remover hobby
    p = imprimir hobbies
    q = sair
''')

while executa == True:

    menuChoice = input("\n>..").lower()

    if menuChoice == 'c':


        print("Aqui está o seu cumprimento" ,  nome , ":")

        print( nome , "vc é muito" , choice(adjetivos) , "e gosta mtt de " , choice(hobbies))
        print( "De nada!")

    elif menuChoice == 'a':
        itemToAdd = input("Adicione o hobby:")
        hobbies.append(itemToAdd)

    elif menuChoice == 'd':

        intemToDelete = input("Insita o hobby a ser removido: ")
        hobbies.remove(ItemToDelete)

    elif menuChoice == 'p':
        print(hobbies)
        

    elif menuChoice == 'q':


            executa = False

    else:
            print("Escolha uma opção válida")
            
