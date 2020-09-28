n = int(input())
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
mu = n // 10000 % 10
md = n // 100000 % 10
mc = n // 1000000 % 10
mm = n // 10000000 % 10

soma= u + d + c + m + mu + md + mc + mm 
print(f'{soma}')
