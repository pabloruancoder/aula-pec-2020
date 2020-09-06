def nome(n):
    a = len(n)
    return a


def conjunge(c):
    a = len(c)
    return a


def main():
    n = str(input(""))
    estado = input("")
    nome(n)
    if estado in 'sS' or estado in '1':
        casal = str(input(""))
        conjunge(c)
    if estado in 'cC' or estado in '1':
        a = nome(n)
        b = conjunge(c)
        print(a + b)
    else:
        print(nome(n))


if __name__ == '__main__' :
    main()