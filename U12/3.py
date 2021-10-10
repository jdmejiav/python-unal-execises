
archivo = open('matrix.txt','r',encoding="utf8")

smith = False
tempPregunta=''
esPregunta=False
preguntas = {}
for renglon in archivo:
    if 'Smith:' in renglon:
        smith=True
    if smith:
        for c in renglon:
            if smith:
                if c=='←':
                    smithFalse=False
                    tempPregunta=''
                    esPregunta=False
                    continue
                if c=='?':
                    if esPregunta:
                        esPregunta=False
                        if (tempPregunta not in preguntas) and (len(tempPregunta.split())>=2):
                            print("?"+tempPregunta.replace('\n',' ')+"?")
                            preguntas[tempPregunta]=1
                            tempPregunta=''
                        else:
                            tempPregunta=''
                    else:
                        tempPregunta=''
                        esPregunta=True
                        continue

                if esPregunta:
                    tempPregunta+=c
    else:
        smithFalse=False
        tempPregunta=''
        esPregunta=False
        continue
