def soma(cont):
    while True:
        n = int(input())
        cont += n
        if n == 0:
            break
    return cont

def main():
    cont = 0
    print(soma(cont))

if __name__ == '__main__':
    main()
