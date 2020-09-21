def cont_divida(salario,divida,mês,ano):
    while True:
        if salario > divida:
            if 1 < mês < 3:
                divida = ((15 / 100) * divida) + divida
                mês += 1
            if mês == 3:
                salario = ((5 / 100 ) * salario) + salario
                divida = ((15 / 100) * divida) + divida
                mês += 1
            elif mês != 3 :
                divida = ((15 / 100) * divida) + divida
                if mês == 12:
                    mês = 1
                    ano +=1
                else:
                    mês +=1
        if salario < divida:  # A flag, pornto de parada da excução do programa.
            break
    return f'{mês}/{ano}'

def main():
    salario = float(input())
    divida = float(input())
    mês = 10
    ano = 2016
    print(cont_divida(salario,divida,mês,ano))

if __name__ == '__main__':
    main()
