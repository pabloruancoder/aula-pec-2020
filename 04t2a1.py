def cont(nome, estado_civil):
    # Precessamento de dados
    if estado_civil == 1:
        nome_conjugue = input('Digite o nome do conjuguê: ')
        return f'A quantidade de caracteres no nome mais o nome do conjuguê {len(nome) + len(nome_conjugue)}'
    else:
        return f'A quantidade de caracteres no nome é {len(nome)}'

def main():
    # Entrada de dados
    nome = input('Digite seu nome: ')
    estado_civil = int(input('Estado Civil [1- Casado/ 2- Solteiro]: '))

    # Saída de dados
    print(cont(nome,estado_civil))

if __name__ == '__main__':
    main()
