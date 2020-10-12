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

def aniversario(diaUsuario,mesUsuario):
    retorno = ''
    cidades = carrega_cidades()
    for ci in cidades:
        if ci[3] == diaUsuario and ci[4] == mesUsuario:
            retorno += f'{ci[:][2]}({ci[:][0]})\n'

    return retorno.strip()

def main():
    diaUsuario = int(input())
    mesUsuario = int(input())
    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {diaUsuario} DE {nomesMeses(mesUsuario)}:')
    print(aniversario(diaUsuario,mesUsuario))

if __name__ == '__main__':
    main()
