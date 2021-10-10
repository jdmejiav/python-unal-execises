n = int(input())


for _ in range (0,n):
    s = int(input())
    matrizInferior = True
    matrizSuperior = True
    for i in range (0,s):
        temp = input()
        matTemp = temp.split()

        for j in range(0,i):
            if float(matTemp[j])!=0:
                matrizSuperior=False

        for j in range(i+1,s):
            if float(matTemp[j])!=0:
                matrizInferior=False

    if matrizSuperior and matrizInferior:
        print("Diagonal")
    elif matrizSuperior:
        print("Triangular superior")
    elif matrizInferior:
        print("Triangular inferior")
    else:
        print("Ni diagonal ni triangular")
