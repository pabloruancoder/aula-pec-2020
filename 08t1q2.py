def sequência(total,lista1,lista2,lista3,lista4):
    retorno = ''
    for c in range(1, total + 1):
        numeros = int(input())
        lista1.insert(0,0)
        lista2.append(c)
        lista3.append(numeros)
        
    for c in range(1,total+1):
        numeros1 = int(input())
        lista4.append(numeros1)

    lista4.reverse()
    retorno = f'{lista1}\n{lista2}\n{lista3}\n{lista4}'

    return retorno

def main():
    total = int(input())
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    print(sequência(total,lista1,lista2,lista3,lista4))

if __name__ == '__main__':
    main()
