
archivo = open('cadena.txt','r')

for renglon in archivo:
    renglon = renglon.replace('\n','')
    if len(renglon)!=0:
        cadena = renglon.split()
        es_cadena=True
        for i in range (0,len(cadena)):
            if i < len(cadena)-1:
                if cadena[i][len(cadena[i])-2:]==cadena[i+1][:2]:
                    es_cadena= False
                elif cadena[i][len(cadena[i])-3:]==cadena[i+1][:3]:
                    es_cadena = False
                else:
                    es_cadena=True
                    break

        if not es_cadena:
            print("cadena completa")
        else:
            print("cadena rota")
    else:
        break
