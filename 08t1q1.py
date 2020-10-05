notas = []
soma = 0
multi =1

for n in range(0 , 10):
    numeros = int(input())
    notas.append(numeros)
    soma += numeros
    multi *= numeros
    
print(f'''{notas}
{soma}
{multi}''')
