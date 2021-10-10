

archivo = open('matrix.txt','r',encoding="utf8")

inicioLinea=True
lineas=[]
temp =""
for renglon in archivo:

    for i in renglon:
        if i!='←':
            temp+=i
        else:
            lineas.append(temp.replace('\n',' '))
            temp=""


preguntas=[]
for i in lineas:
    bandera=False
    lineaTemp=''
    if 'Smith:' in i:

        for c in i:
            if c == '?':

                if bandera:
                    bandera=False
                    if lineaTemp not in preguntas and len(lineaTemp.split())>=2:
                        print("?"+lineaTemp+"?")
                        preguntas.append(lineaTemp)
                    lineaTemp=''
                else:
                    bandera=True
            else:
                if bandera:
                    lineaTemp+=c
    else:
        continue
archivo.close()
