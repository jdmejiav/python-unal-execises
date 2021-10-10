
n = int(input())
salida = []

for k in range(0,n):
    entrada = input()
    f = 0
    m = 0
    for i in entrada:
        if i=="F":
            f+=1
        elif i=="M":
            m+=1

    if f==m:
        salida.append("Es posible hacer un unico circulo")
    else:
        salida.append("No es posible")
print()
for i in salida:
    print(i)
