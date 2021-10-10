from datetime import datetime

n = int(input())

for i in range(0,n):
    entrada = input()
    fecha = entrada.split()
    inicio = datetime.strptime(fecha[1],'%Y-%m-%d')
    fin = datetime.strptime(fecha[2],'%Y-%m-%d')

    tiempo = fin - inicio

    print(str(tiempo.days)+" dias = "+str(int(tiempo.days)*24)+" horas = "+str(int(tiempo.days)*24*60)+" minutos = "+str(int(tiempo.days)*24*3600)+" segundos")
