nome = input("Calculadora do Amor")
for char in nome:
    print(char)
alfabeto = "abcdefghijklmnopqrstuvwxyz"

mensagem = input("Digite o nome de 2 pessoas: ").lower()

mensagemCriptografada = ""
chave = input("Seu placar de compatibilidade: 80")
chave = int(chave)

for char in mensagem:
    if char in alfabeto:

        posicao = alfabeto.find(char)

novaPosicao = (posicao + chave) % 26
mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]
   else:

        mensagemCriptografada = mensagemCriptografa + char

print("Vocês terão um relacionamento muito intenso! <3" , mensagemCriptografada)
