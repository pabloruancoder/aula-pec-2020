def cardapio():
    return('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')

def main():
    H = 5.50
    C = 6.80
    M = 4.50
    A = 7.00
    Q = 4.00
    valor = resultado = 0
    while True:
        print(cardapio())
        código = input().upper()[0]
        if código == 'H':
            valor += H
        elif código == 'C':
            valor += C
        elif código == 'M':
            valor += M
        elif código == 'A':
            valor += A
        elif código == 'Q':
            valor += Q
        elif código == 'X':
            break
    if valor == 0:
        False
    else:
        resultado = f'{valor:.2f}'
    return resultado

if __name__ == '__main__':
    resultado = main()
    if resultado != 0:
        print(resultado)
