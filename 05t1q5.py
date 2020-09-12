maior = 0
menor = 0
for num in range(1,101):
    valor = int(input())
    if num == 0:
        maior = menor = valor
    else:
        if valor > maior:
           maior = valor
print(maior)
