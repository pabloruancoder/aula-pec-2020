def maior_menor():
    maior = menor = cont = resultado = 0
    while True:
        numero = int(input())
        if numero != 0:
            cont += 1
            if cont == 1:
                maior = menor = numero
            else:
                if numero > maior:
                    maior = numero
                if numero < menor:
                    menor = numero
        if numero == 0:
            break
    if cont == 0:
        False
    if cont != 0:
        resultado = f'{maior}\n{menor}'
    return resultado

def main():
    r =  maior_menor()
    if r != 0:
        print(r)
    

if __name__ == '__main__':
    main() 
