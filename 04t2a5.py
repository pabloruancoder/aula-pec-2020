def ordem_crescente(a,b,c):
    # Procesamneto de dados
    numero1 = numero2 = numero3 = 0
    if ( c < a > b):
        numero3 = a
        if (b > c):
           numero2 = b
           numero1 = c
        else:
           numero2 = c
           numero1 = b

    elif ( a < b > c):
        numero3 = b
        if (c > a):
            numero2 = c
            numero1 = a
        else:
            numero2 = a
            numero1 = c

    elif (b < c > a):
        numero3 = c
        if (b > a):
            numero2 = b
            numero1 = a
        else:
            numero2 = a
            numero1 = b
    
    return f'Os números digitados na ordem crescente é {numero1}, {numero2}, {numero3}'

def main():
    # Entrada de dados
    num1 = int(input('Digite o 1° número: '))
    num2 = int(input('Digite o 2° número: '))
    num3 = int(input('Digite o 3° número: '))

    # Saída dos dados
    print(ordem_crescente(num1,num2,num3))

if __name__ == '__main__':
    main()
