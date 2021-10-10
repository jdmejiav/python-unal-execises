from datetime import datetime,timedelta
n = int(input())
ultimoDia=None
prom=timedelta(0)
for i in range (0,n):
    entrada = input()
    fecha = entrada.split()
    actual = datetime.strptime(fecha[0]+"_"+fecha[1],'%Y-%m-%d_%H:%M:%S')
    if ultimoDia ==None:
        ultimoDia= actual
    else:
        dif = actual - ultimoDia
        print(str(dif.days)+" dias, "+str(dif.seconds//3600)+" horas, "+str(((dif.seconds//60)%60))+" minutos, "+str(dif.seconds%60)+" segundos")
        prom += (actual-ultimoDia)
        ultimoDia = actual


prom=prom/(n-1)
print("Promedio: "+str(prom.days)+" dias, "+str(prom.seconds//3600)+" horas, "+str(int((prom.seconds/60)%60))+" minutos, "+str(int(prom.seconds%60))+" segundos")
