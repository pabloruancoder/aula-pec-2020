def verifica_digito(caracter):
    digito =(caracter)
    return caracter in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZaeiouAEIOU'

def main():
    digito = input()
    print(verifica_digito(digito))
if __name__ == '__main__':
    main()
