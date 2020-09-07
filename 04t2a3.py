def leia_num(numero):
    # procesaamneto de dados 
    dezena = numero // 10 % 10
    unidade = numero // 1 % 10
    if (dezena % 2 == 0 and unidade % 2 == 0):
        return 'Nenhum dígito é ímpar.'
    elif (dezena % 2 != 0 and unidade % 2 == 0 or 
            dezena % 2 == 0 and unidade % 2 != 0):
            return 'Apenas um dígito é ímpar.'
    else:
        return 'Os dois dígitos são ímpares.'

def main():
    # Entrada de dados
    num = int(input('Digite um número entre 10 a 99: '))

    # Verifica se a entrada é válida
    if (10 <= num <= 99):
        print(leia_num(num))
    # se não for o programa para
    else:
        False

if __name__ == '__main__':
    main()
