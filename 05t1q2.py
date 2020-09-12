par = 0
impares = 0
for num in range(1,101):
    valor = int(input())
    if valor % 2 == 0:
        par += 1
    else:
        impares += 1
print(par)
print(impares)
