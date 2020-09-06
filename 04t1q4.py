num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

media = (num1 + num2 + num3 + num4 + num5)/5

print(f'{media}')
if media < num1:
           print(f'{num1:.2f}')
elif media < num2:
           print(f'{num2:.2f}')
elif media < num3:
           print(f'{num3:.2f}')
elif media < num4:
           print(f'{num4:.2f}')
elif media < num5:
           print(f'{num5:.2f}')

           
