from datetime import datetime

n = int(input())


for i in range(0,n):
        entrada = input()
        fecha = datetime.strptime(entrada,'%I:%M:%S %p')
        segundos = fecha.hour*3600+fecha.minute*60+fecha.second
        porcentaje = round((segundos*100)/86400,3)
        print("Loading day ... "+str(porcentaje)+"%")
