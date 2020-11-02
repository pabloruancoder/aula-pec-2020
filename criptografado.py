alfabeto = "abcdefghijklmnopqrstuvwxyz"
chave = 7
letra = input(" Por favot, entre com uma letra para criptografar: ")

posicao = alfabeto.find(letra)

novaPosicao = (posicao - chave) % 26
letraCriptografada = alfabeto[novaPosicao]

print("Sua letra criptografada é" , letraCriptografada)
