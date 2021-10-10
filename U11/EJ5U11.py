from datetime import datetime

n = int(input())

nVeces=0
prom = None
for i in range (0,n):
    entrada=input()
    actividad = entrada.replace(' ','').split(",")
    if actividad[1]=='barberia':
        nVeces = nVeces+1
        ini = datetime.strptime(actividad[0]+"_"+actividad[2],"%Y-%m-%d_%H:%M:%S")
        fin = datetime.strptime(actividad[0]+"_"+actividad[3],"%Y-%m-%d_%H:%M:%S")
        if prom != None:
            prom = prom+(fin-ini)
        else:
            prom = fin-ini

print(str(nVeces)+" veces")
prom = prom/nVeces
print(str(prom.seconds//3600)+" horas, "+str(int((prom.seconds/60)%60))+" minutos, "+str(int(prom.seconds%60))+" segundos")
