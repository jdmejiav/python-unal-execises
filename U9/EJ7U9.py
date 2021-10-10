n = int(input())
salida = []

for k in range(0,n):
    entrada = input()
    temp = ""
    i=0
    while i < len(entrada):
        if entrada[i]=="_":
            i+=1
            if i<len(entrada):
                try:
                    if entrada[i+1]!="_":
                        temp+=entrada[i].upper()
                except:
                    continue
        else:
            if i==0:
                temp+=entrada[i].upper()
            else:
                temp+=entrada[i]
        i+=1
    salida.append(temp)

for i in salida:
    print(i)
