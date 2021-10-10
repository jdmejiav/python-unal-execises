from random import randint

n = int(input())

for i in range(0,n):
    temp = input()
    cartas = temp.split()
    puntosH=0
    puntosP=0
    for i in cartas:
        tempN = randint(1,13)
        if int(i) > tempN:
            puntosP+=1
        elif int(i) < tempN:
            puntosH+=1
    print("Puntos humano: "+str(puntosH)+" Puntos plataforma: "+str(puntosP))
