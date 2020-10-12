def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def nomesMeses(mes):
    if mes == 1:
        return 'JANEIRO'
    elif mes == 2:
        return 'FEVEREIRO'
    elif mes == 3:
        return 'MARÇO'
    elif mes == 4:
        return 'ABRIL'
    elif mes == 5:
        return 'MAIO'
    elif mes == 6:
        return 'JUNHO'
    elif mes == 7:
        return 'JULHO'
    elif mes == 8:
        return 'AGOSTO'
    elif mes == 9:
        return 'SETEMBRO'
    elif mes == 10:
        return 'OUTUBRO'
    elif mes == 11:
        return 'NOVEMBRO'
    elif mes == 12:
        return 'DEZEMBRO'

def aniversario(mes,pop):
    retorno = ''
    cidades = carrega_cidades()
    for ci in cidades:
        if ci[4] == mes and ci[5] > pop:
            retorno += (f'{ci[:][2]}({ci[:][0]}) tem {ci[:][5]} habitantes e faz aniversário em '
                        f'{ci[:][3]} de {nomesMeses(mes).lower()}.\n')

    return retorno.strip()

def main():
    mes = int(input())
    pop = int(input())
    print(f'CIDADES COM MAIS DE {pop} HABITANTES E ANIVERSÁRIO EM {nomesMeses(mes)}:')
    print(aniversario(mes,pop))

if __name__ == '__main__':
    main()
