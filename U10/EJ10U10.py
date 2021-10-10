n = int(input())

for _ in range(0,n):
    caso = input()
    cuadrado = []
    constante = 0
    for _ in range(0,4):
        temp = input()
        temp_ent = temp.split()
        temp2 = []
        for numero in temp_ent:
            temp2.append(int(numero))
            constante+=int(numero)
        cuadrado.append(temp2)

    constante=int(constante/4)
    diagonal1 = 0
    diagonal2 = 0
    fila = 0

    col0=0
    col1=0
    col2=0
    col3=0
    flag =True
    while fila<4:
        diagonal1+=cuadrado[fila][fila]
        diagonal2+=cuadrado[3-fila][fila]
        col0+=cuadrado[fila][0]
        col1+=cuadrado[fila][1]
        col2+=cuadrado[fila][2]
        col3+=cuadrado[fila][3]
        temp = 0
        columna = 0
        while columna <4:
            temp+=cuadrado[fila][columna]

            columna+=1
        if temp!=constante:
            flag=False
            break
        fila+=1

    if diagonal1!=constante or diagonal2!=constante or col0!=constante or col1!=constante or col2!=constante or col3!=constante:
        flag=False

    if flag:
        print("Cuadrado magico")
    else:
        print("Cuadrado muggle")
