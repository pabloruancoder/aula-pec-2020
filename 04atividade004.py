def verifica_digito(caracter):
    digito =(caracter)
    return caracter in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxz'

def main():
    digito = input()
    print(verifica_digito(digito))
if __name__ == '__main__':
    main()
