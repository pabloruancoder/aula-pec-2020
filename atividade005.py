def numero1(desconto, prestimo1, prestimo2):
    def main():
            numero1 = float(input())
            desconto = (numero1 * 0.9)
            prestimo1 = (numero1 * 5)
            prestimo2 = (numero1 * 10 * 0.17)

print("{},{},{}".format(desconto,prestimo1,prestimo2))
if __name__=="__main__":
        main()
