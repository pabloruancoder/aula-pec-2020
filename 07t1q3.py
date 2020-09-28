def amaior(paisa, paisb, tempo):
    while paisa > paisb:
        paisa *= 1.02
        paisb *= 1.03
        tempo += 1
        if paisa < paisb:
            break
    print(f'{tempo}')

def bmaior(paisa, paisb, tempo):
    while paisa < paisb:
        paisa *= 1.03
        paisb *= 1.02
        tempo += 1
        if paisa > paisb:
            break
    print(f'{tempo}')

def main():
    paisa = float(input())
    paisb = float(input())
    tempo = 0
    if paisa > paisb:
        amaior(paisa, paisb, tempo)
    elif paisa < paisb:
        bmaior(paisa, paisb, tempo)
if __name__ == '__main__':
    main()



    

    
    
