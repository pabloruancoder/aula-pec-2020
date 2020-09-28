num = int(input())
for c in range(num + 1):
    if num % c == 0:
        num = num
    else:
        print(f'{c}')
