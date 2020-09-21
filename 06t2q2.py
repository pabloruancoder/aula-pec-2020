def dados():
    cont = soma = maior = menor = media = resultado = 0
    while True:
        i = int(input())
        if i != 0:
            cont += 1 
            soma += i
            media = soma / cont 
            if cont == 1:
                maior = menor = i
            else:
                if i > maior:
                    maior = i
                if i < menor:
                    menor = i
        if i == 0:
            break
    if cont == 0 :
        False
    if cont != 0:
        resultado = f'{cont}\n{media:.2f}\n{menor}\n{maior}'
    return resultado

def main():
    res = dados()
    if res != 0:
        print (res)

if __name__ == '__main__':
    main()
