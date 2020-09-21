def respostas(opcao):
    if opcao == 1:
        return '1 - Olá. Como vai?'
    elif opcao == 2:
        return '2 - Vamos estudar mais.'
    elif opcao == 3:
        return '3 - Meus Parabéns!'
    elif opcao == 0:
        return '0 - Fim de serviço.'
    else:
        return 'Opção inválida.'

def main():
    while True:
        print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
        opção = int(input())
        print(respostas(opção))
        if opção == 0:
            break
if __name__ == '__main__':
    main()
