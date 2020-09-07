def signo(dia,mes):
    # Processamento de dados, verifica qual o signo do usúario 
    if (31 >= dia >= 21 and mes == 3) or ( 1 <= dia <= 19 and mes == 4):
        return'Seu signo é Áries'
    elif (30 >= dia >= 20 and mes == 4) or (1 <= dia <= 20 and mes == 5):
        return'Seu signo é Touro'
    elif (31 >= dia >= 21 and mes == 5 ) or (1 <= dia <= 21 and mes == 6):
        return'Seu signo é Gêmeos'
    elif (30 >= dia >= 22 and mes == 6) or (1 <= dia <= 22 and mes == 7):
        return'Seu signo é Câncer'
    elif (31 >= dia >= 23 and mes == 7) or (1 <= dia <= 22 and mes == 8):
        return'Seu signo é Leão'
    elif (31 >= dia >= 23 and mes == 8) or (1 <= dia <= 22 and mes == 9):
        return'Seu signo é Virgem'
    elif (30 >= dia >= 23 and mes == 9) or (1 <= dia <= 22 and mes == 10):
       return'Seu signo é Libra'
    elif (31 >= dia >= 23 and mes == 10) or (1 <= dia <= 21 and mes == 11):
       return'Seu signo é Escorpião'
    elif (30 >= dia >= 22 and mes == 11) or (1 <= dia <= 21 and mes == 12):
        return'Seu signo é Sagitário'
    elif (31 >= dia >= 22 and mes == 12) or (1 <= dia <= 19 and mes == 1):
        return'Seu signo é Capricórnio'
    elif (31 >= dia >= 20 and mes == 1) or (1 <= dia <= 18 and mes == 2):
        return'Seu signo é Aquário'
    elif (29 >= dia >= 19 and mes == 2) or (1 <= dia <= 20 and mes == 3):
        return'Seu signo é Peixes'

def main():
    # Entrada de dados
    dia = int(input('Digite o dia do seu nascimento: '))
    mes = int(input('Digite o mês do nascimento: '))

    # Saída de dados
    print(signo(dia, mes))

if __name__ == '__main__':
    main()