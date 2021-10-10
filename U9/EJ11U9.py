archivo = open('trifelios.txt','r')

def separar(renglon):
    retorno = []
    retorno.append(renglon[:int(len(renglon)/2)])
    retorno.append(renglon[int(len(renglon)/2):])
    return retorno
def separar1(renglon):
    retorno = []
    retorno.append(renglon[:int(len(renglon)/2)-1])
    retorno.append(renglon[int(len(renglon)/2)-1:])
    return retorno

def separar2(renglon):
    retorno = []
    retorno.append(renglon[:int(len(renglon)/2)+1])
    retorno.append(renglon[int(len(renglon)/2)+1:])
    return retorno
def separar3(renglon):
    retorno = []
    retorno.append(renglon[:int(len(renglon)/2)+2])
    retorno.append(renglon[int(len(renglon)/2)+2:])
    return retorno
def separar4(renglon):
    retorno = []
    retorno.append(renglon[:int(len(renglon)/2)-2])
    retorno.append(renglon[int(len(renglon)/2)-2:])
    return retorno



for renglon in archivo:
    renglon = renglon.replace('\n','')
    trifelio = renglon.split('-')

    if len(renglon)!=0:
        palabra1 = separar(trifelio[0])
        palabra2 = separar(trifelio[1])

        temp = palabra1[0]+palabra1[1]
        temp2 = palabra2[1]+palabra2[0]

        if temp == temp2:
            print('Es trifelio')
        else:
            palabra1 = separar1(trifelio[0])
            palabra2 = separar1(trifelio[1])

            temp = palabra1[0]+palabra1[1]
            temp2 = palabra2[1]+palabra2[0]
            if temp == temp2:
                print('Es trifelio')
            else:
                palabra1 = separar2(trifelio[0])
                palabra2 = separar2(trifelio[1])

                temp = palabra1[0]+palabra1[1]
                temp2 = palabra2[1]+palabra2[0]
                if temp == temp2:
                    print('Es trifelio')
                else:
                    palabra1 = separar3(trifelio[0])
                    palabra2 = separar3(trifelio[1])

                    temp = palabra1[0]+palabra1[1]
                    temp2 = palabra2[1]+palabra2[0]
                    if temp == temp2:
                        print('Es trifelio')
                    else:
                        palabra1 = separar4(trifelio[0])
                        palabra2 = separar4(trifelio[1])

                        temp = palabra1[0]+palabra1[1]
                        temp2 = palabra2[1]+palabra2[0]
                        if temp == temp2:
                            print('Es trifelio')
                        else:
                            print('No es trifelio')
archivo.close()
