def inicial(n,taxa):
    quantidade = 0
    dobro = n * 2
    while n < dobro:
        juros = (taxa / 100) * n
        n += juros
        quantidade +=1
    return quantidade

def main():
    n = float(input())
    taxa = float(input())
    qtd = inicial(n,taxa)

    print(f'{qtd:.2f}')

if __name__ == '__main__':
        main()
