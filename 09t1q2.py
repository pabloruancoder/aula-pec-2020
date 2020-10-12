def convertFarenheit(n):
    return (n * (9/5)) + 32

def convertCelsius(n):
    return (n - 32) * (5/9)

def graus(temp1,escala1,temp2,escala2):
    dados = ()
    if escala1 == 'C' and escala2 == 'C':
        soma = temp1 + temp2
        dados = (soma, 'C')

    elif escala1 == 'F' and escala2 == 'F':
        soma = temp1 + temp2
        dados = (soma, 'F')

    elif escala1 == 'F' and escala2 == 'C':
        soma = convertCelsius(temp1) + temp2
        dados = (round(soma, 4), 'C')

    elif escala1 == 'C' and escala2 == 'F':
        soma = convertFarenheit(temp1) + temp2
        dados = (round(soma, 4), 'F')

    return dados
def main(): 
    temp1 = float(input())
    escala1 = input().upper()[0]

    temp2 = float(input())
    escala2 = input().upper()[0]
    print(graus(temp1,escala1,temp2,escala2))

if __name__ == '__main__':
    main()
