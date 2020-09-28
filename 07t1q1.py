tempo = 0
vantagem = int(input())
tartaruga = vantagem
lebre = 0

if vantagem >= 9:
    while tartaruga >= lebre:
        tartaruga += 1
        lebre += 10
        tempo += 1
        if tartaruga <= lebre:
            break
    print(f'{tempo}')

elif vantagem <=9:
    print(f'{tempo}')
