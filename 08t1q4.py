def contador(listaNumeros):
    for c in range(1, 21):
        n = int(input())
        listaNumeros[0].append(n)
        if n % 2 == 0:
            listaNumeros[1].append(n)
        else:
            listaNumeros[2].append(n)

    return f'{listaNumeros[0]}\n{listaNumeros[1]}\n{listaNumeros[2]}'

def main():
    listaNumeros = [[], [], []]
    print(contador(listaNumeros))

if __name__ == '__main__':
    main()