def conceito():
    while True:
        nota = float(input())
        conceito = ''
        if nota >= 8.5 and nota <= 10:
            conceito = 'A'
            break
        elif nota >= 7.0 and nota < 8.5:
            conceito = 'B'
            break
        elif nota >= 5.0 and nota < 7.0:
            conceito = 'C'
            break
        elif nota >= 4.0 and nota < 5.0:
            conceito = 'D'
            break
        elif nota >= 0 and nota < 4.0:
            conceito = 'E'
            break
        else:
            print('Nota inválida.')

    return conceito

def main():
    resultado = conceito()
    print(resultado)

if __name__ == '__main__':
    main()
