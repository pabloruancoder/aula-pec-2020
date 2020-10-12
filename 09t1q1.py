def convertFarenheit(n):
    return (n * (9/5)) + 32

def convertCelsius(n):
    return (n - 32) * (5/9)

def graus(temp1,escala1,temp2,escala2):
    maior = 0
    dados = ()
    e = ''
    if escala1 == 'C' and escala2 == 'C':
        if temp1 > temp2:
            maior = temp1
        else:
            maior = temp2
        dados = (maior, 'C')

    elif escala1 == 'F' and escala2 == 'F':
        if temp1 > temp2:
            maior = temp1
        else:
            maior = temp2
        dados = (maior, 'F')
    
    elif escala1 == 'F' and escala2 == 'C':
        if convertFarenheit(temp2) > temp1:
            maior = temp2
            e = escala2
        else:
            maior = temp1
            e = escala1
        dados = (maior,e)

    elif escala1 == 'C' and escala2 == 'F':
        if convertCelsius(temp2) > temp1:
            maior = temp2
            e = escala2
        else:
            maior = temp1
            e = escala1
        dados = (maior, e)
    return dados
    
def main(): 
    temp1 = float(input())
    escala1 = input().upper()[0]

    temp2 = float(input())
    escala2 = input().upper()[0]
    print(graus(temp1,escala1,temp2,escala2))

if __name__ == '__main__':
    main()
