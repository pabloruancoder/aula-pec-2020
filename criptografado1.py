nome = input("Qual seu nome? ")
for char in nome:
    print(char)
alfabeto = "abcdefghijklmnopqrstuvwxyz"

mensagem = input(" Por favot, entre com uma letra para criptografar: ").lower()

mensagemCriptografada = ""
chave = input("Por favor, entre a chave: ")
chave = int(chave)

for char in mensagem:
    if char in alfabeto:

        posicao = alfabeto.find(char)

novaPosicao = (posicao + chave) % 26
mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]
   else:

        mensagemCriptografada = mensagemCriptografa + char

print("Sua letra criptografada é" , mensagemCriptografada)
