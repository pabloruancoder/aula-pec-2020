def num_int(inicio,fim):
    numeros = ""
    
    for num in range(inicio,fim + 1):
        numeros += str(num) + '\n'
    return numeros.strip()

def main():
    inicio = 1
    fim = 50
    print(num_int(inicio, fim))

if __name__=='__main__':
    main()
