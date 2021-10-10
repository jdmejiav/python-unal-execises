from datetime import datetime
n = int(input())

for i in range(0,n):
    temp = input()
    entrada = temp.split()
    fechaIni = datetime.strptime(entrada[0],'%d-%m-%Y')
    fechaFin = datetime.strptime(entrada[1],'%d-%m-%Y')
    delta = fechaFin-fechaIni
    salida = ""
    for i in range (0,delta.days//5):
        salida+="5 "
    for i in range (0,delta.days%5):
        salida+="1 "
    print(salida[0:len(salida)-1])
