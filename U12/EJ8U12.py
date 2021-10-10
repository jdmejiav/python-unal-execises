j = int (input())

for _ in range (0,j):
    rubik = []
    n = int(input())
    for i in range(1,n+1):
        temp = []
        for j in range(1,n+1):
            temp.append(j)
        rubik.append(temp)
    movimientos = input()
    temp = movimientos.split()
    for movimiento in temp:
        if movimiento[0]=="F":
            fila = int (movimiento[1])-1
            if movimiento[2]=="-":
                rubik[fila] = rubik[fila][1:]+[rubik[fila][0]]
            if movimiento[2]=="+":
                rubik[fila] = [rubik[fila][n-1]]+rubik[fila][:-1]
        elif movimiento[0]=="C":
            columna = int(movimiento[1])-1

            if movimiento[2]=="+":
                cola = rubik[n-1][columna]+1
                ultimoMov = rubik[0][columna]
                for fila in range(1,n):
                    temp2= rubik[fila][columna]
                    rubik[fila][columna]=ultimoMov
                    ultimoMov=temp2
                rubik[0][columna]=cola-1

            elif movimiento[2]=="-":
                columna = int(movimiento[1])-1
                inicio = rubik[0][columna]
                for fila in range(0,n-1):
                    rubik[fila][columna]=rubik[fila+1][columna]
                rubik[n-1][columna] = inicio
    for fila in range(0,n):
        sal=""
        for columna in range(0,n):
            sal+=str(rubik[fila][columna])
        print(sal)
    print()
