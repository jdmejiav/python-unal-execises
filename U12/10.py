n = int (input())

for _ in range(0,n):
    entrada = input()
    sudoku=[]
    tempFilas=[]
    for i in range(0,9):
        bandera = True
        entrada= input()
        temp = entrada.split()
        sudoku.append(temp)
        dic={
                "1":False,
                "2":False,
                "3":False,
                "4":False,
                "5":False,
                "6":False,
                "7":False,
                "8":False,
                "9":False,
        }
        for j in temp:
            if not dic[j]:
                dic[j]=True
            else:
                bandera=False


    for col in range (0,9):
        dic={
                "1":False,
                "2":False,
                "3":False,
                "4":False,
                "5":False,
                "6":False,
                "7":False,
                "8":False,
                "9":False,
        }
        for fila in range (0,9):
            if not dic[sudoku[fila][col]]:
                dic[sudoku[fila][col]]=True
            else:
                bandera=False

    if bandera:
        print("Resuelto")
    else:
        print("No resuelto")
