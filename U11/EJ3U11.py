from random import randint
n = int(input())
for  i in range(0,n):
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    resultado = dado1+dado2
    plataforma = int(input())
    if plataforma >resultado:
        print("Gana la plataforma")
    elif plataforma<resultado:
        print("Gana el humano")
    elif plataforma==resultado:
        print("Empate")
