n = int(input())

top = []

for i in range (0,n):
    entrada = input()
    trabajador = entrada.split(",")
    IMC = round(float(trabajador[1])/float(trabajador[2])**2,1)

    if IMC > 25 and float(trabajador[3].replace(' ','')) >= 100.0 and float(trabajador[4].replace(' ',''))>150:
        top.append([trabajador[0],IMC])

top.sort(key = lambda x: (x[1],x[0]),reverse=True )

for i in range(0,len(top)):
        print(str(i+1)+" "+top[i][0]+" "+str(top[i][1]))
