def cont_pares(numero):
    # processamento de dados
    cont = 0
    centena = numero // 100 % 10
    dezena = numero // 10 % 10
    unidade = numero // 1 % 10
    # verifica se a centena é um numero PAR
    if centena % 2 == 0:
        if dezena % 2 == 0 and unidade % 2 == 0:
            cont += 3
        elif dezena % 2 != 0 and unidade % 2 == 0:
            cont += 2
        elif dezena % 2 == 0 and unidade % 2 != 0:
            cont += 2
        elif dezena % 2 != 0 and unidade % 2 != 0:
            cont += 1
    # verifica se a centena não for um número PAR
    elif centena % 2 != 0:
        if dezena % 2 == 0 and unidade % 2 == 0:
            cont += 2
        elif dezena % 2 != 0 and unidade % 2 == 0:
            cont += 1
        elif dezena % 2 == 0 and unidade % 2 != 0:
            cont += 1
        elif dezena % 2 != 0  and unidade % 2 != 0:
            cont += 0
    # Verifica se a dezena é um nuúmero PAR
    elif dezena % 2 == 0:
        if unidade % 2 == 0:
            cont += 2
        else:
            cont
    # Verifica se a dezena não é um número PAR
    elif dezena % 2 != 0:
        cont
        if unidade % 2 == 0:
            cont += 1
        else:
            cont
    # Verifica se a dezena é um número PAR
    elif unidade % 2 == 0:
        cont += 1
    # Verifica se a unidade é um número IMPAR
    elif unidade % 2 != 0:
        cont

    return f'O número {numero} tem {cont} números pares'
def main():
    # Entradad de dados
    numero = int(input('Digite um número entre 100 a 999: '))

    # Condição verdadeira
    if (100 <= numero <= 999):
        print(cont_pares(numero))

    # Se a condição for falso o programa para
    else:
        False

if __name__ == '__main__':
    main()