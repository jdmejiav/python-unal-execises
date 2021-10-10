
archivo = open('conversaciones.txt','r')

for renglon in archivo:
    renglon = renglon.replace('\n','').lower()
    opositivos = 0
    causativos = 0

    if "sin embargo" in renglon:
        opositivos+=1

    if "no obstante" in renglon:
        opositivos+=1

    if "ahora bien" in renglon:
        opositivos+=1

    if "aun asi" in renglon:
        opositivos+=1


    if "por tanto" in renglon:
        causativos+=1

    if "dado que" in renglon:
        causativos+=1

    if "por consiguiente" in renglon:
        causativos+=1

    if "asi pues" in renglon:
        causativos+=1

    if "por ende" in renglon:
        causativos+=1

    print("Opositivos "+str(opositivos)+" Causativos "+str(causativos))

archivo.close()
