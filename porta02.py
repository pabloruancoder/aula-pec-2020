from random import*
jogando = True
score = 0
print('''
Porta da Fortuna!!
==================

Existem um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o premio!!

  ________   ________   ________
  |      |   |      |   |      |
  |      |   |      |   |      |
  |[1]   |   |[2]   |   |[3]   |
  |   0  |   |   0  |   |   o  |
  |      |   |      |   |      |
  ________   ________   ________
  ''')
while jogando == True:

        print("\nEscolha uma porta [1, 2 ou 3]")
        portaEscolhida = input()
        portaEscolhida = int(portaEscolhida)

        portaCerta = randint(1,3)

        print("A porta escolhida foi a", portaEscolhida)
        print("A porta certa é a ", portaCerta)

        if portaEscolhida == portaCerta:
            print("Parabéns!")
        else:
            print("Que peninha!!")
        print("Sua pontuação é", score)
        print("\nVocê que jogar de novo? (sim/nao)")
        resposta = input()
        if resposta == 'nao':
            jogando = False

        print("Obrigado por jogar.")
        print("Sua pontuação final é de", score)
                  

