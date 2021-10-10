archivo = open('cameos.txt', 'r')
for linea in archivo:
    linea=linea.lower()
    saramago = "saramago"

    nVeces=0
    for i in linea:
        if i==saramago[0]:

            saramago=saramago[1:]
            if len(saramago)==0:
                saramago="saramago"
                nVeces+=1

    print(nVeces)
archivo.close()
