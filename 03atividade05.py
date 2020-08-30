aluno1 = int(input("Nota 01:"))
aluno2 = int(input("Nota 02:"))
aluno3 = int(input("Nota 03:"))


if aluno3 > 8:
        resultado1 = (aluno1 + aluno2)+(aluno3 + 1)/3
        print(f'{resultado1}')
else:
    resultado = (aluno1 + aluno2 + aluno3)/3
    print(f'{resultado}')
