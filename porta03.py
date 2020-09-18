from random import*
tentativas = 0
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
while score < 3:
    tentativas = tentativas + 1

    print("\nTentativa", tentativas, ": Escolhe um porta(1, 2 or 3):")
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    portaCerta = randint(1,3)

    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a ", portaCerta)

    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score = score + 1
    else:
        print("Que peninha!!")

    print("Sua pontuação é", score)
print("\n** Você conseguiu! Terminou o jogo em",
      tentativas, "tentativas **")
