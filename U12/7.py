n = int(input())

def encontrarCamino(viajes,temp,camino,CaminoActual,llaves):
    if temp == "C-137" and CaminoActual!=0:
        camino.append(CaminoActual)
        return camino
    else:
        if temp in llaves:
            for i in viajes[temp]:
                caminos=encontrarCamino(viajes,i,camino,CaminoActual+1,llaves)
                return caminos
        else:
            camino.append(-1)
            return camino

for _ in range (0,n):
    cant = int(input())
    viajes = {}
    inicio = "C-137"
    final= ""
    llaves = []
    for j in range(0,cant):

        temp = input()
        dest = temp.split()
        if dest[0] not in viajes:
            llaves.append(dest[0])
            viajes[dest[0]]=[dest[1]]
        else:
            viajes[dest[0]].append(dest[1])
        final=dest[1]



    camino = encontrarCamino(viajes,inicio,[],0,llaves)
    bandera=True
    camino.sort()
    for i in camino:
        if i != -1:
            print("Pueden volver a C-137 en "+str(i)+" saltos")
            bandera=False
            break
    if bandera:
        print("Deambulan por el multiverso")
