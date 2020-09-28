meses = 0
poupanca = 10000
preco = float(input(""))

if poupanca <= preco:
    while poupanca <= preco: #enquanto a poupaça for menor que o valor do carro
        meses += 1 # aumenta um mês 
        poupanca *= 1.007 # aumento da renda de 7%
        preco *= 1.004 # aumento da taxa de 4%
        if poupanca >= preco:
            break
    print(f'{meses}')

elif poupanca >= preco:
    print(f'{meses}')


