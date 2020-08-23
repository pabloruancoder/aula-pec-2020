seg = int(input())
horas = seg // 3600
res =seg % 3600
minu = res // 60
segundos = res % 60
print(f'{horas}:{minu}:{segundos}')

