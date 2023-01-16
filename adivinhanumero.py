import random 

max = 1000
numero = random.randint(1, max)

while True:
    tentativa = int(input(f"Adivinhe o número que estou pensando, está entre 1 e {max}: "))
    if tentativa == numero:
        print("\nUau, você acertou!")
        break
    else:
        tentativa = tentativa > numero
        match tentativa:
            case True:
                print("\nErrou pra cima.\n")
            case False:
                print("\nErrou pra baixo\n")