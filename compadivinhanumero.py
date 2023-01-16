import random

def computador_adivinha(x):
    min = 1
    max = x

    while True:
        tentativa = random.randint(min, max)
        correcao = input(f'O número {tentativa} está certo (=), maior (>) ou menor (<)? ')
        if correcao == '=':
            print('Eba, acertou!')
            break
        elif correcao == '>':
            max = tentativa - 1
        elif correcao == '<':
            min = tentativa + 1

computador_adivinha(100000)