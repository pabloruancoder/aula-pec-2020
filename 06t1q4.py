def inverte(n):
    sequência = 0
    while n > 0:
        digito_invertido =  n % 10
        n //= 10
        sequência = sequência * 10 + digito_invertido
    return sequência
def main():
    n = int(input())
    print(inverte(n))

if __name__ == '__main__':
    main()
