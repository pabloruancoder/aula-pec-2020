maior = 0
menor = int(input(''))
for i in range(4):
    p = int(input(''))
    if p>maior:
        maior = p
    if p<menor:
        menor = p
print(f'{maior}')
print(f'{menor}')
