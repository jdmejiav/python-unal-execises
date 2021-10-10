n = int(input())
dic= {}
id = []
promedios = []
for j in range(0,n):
    entrada = input()
    split = entrada.split(",")
    temp=int(split[0])
    id.append(temp)
    promedio = 0.0
    for i in range(1,13):
        if i==4 or i==8:
            promedio += round(float(split[i])/8*5,1)
        elif i==1 or i==6 or i == 11:
            promedio += round(float(split[i])/9*5,1)
        elif i==10 or i==12:
            promedio += round(float(split[i])/10*5,1)
        elif i==2 or i==7 or i==9:
            promedio += round(float(split[i])/11*5,1)
        elif i==3 or i==5:
            promedio += round(float(split[i])/12*5,1)

    dic[temp] = round(promedio/12,1)
    promedios.append(round(promedio/12,1))


idOrd = sorted(id)

for i in range(0,len(idOrd)):
    print(str(idOrd[i])+" "+str(dic[idOrd[i]]))
