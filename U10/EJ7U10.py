n = int(input())
dic = {}

vendedores = []
cant_vendedores = []

for i in range(0,n):
    entrada = input()

    try:
        dic[vendedor[0]]+=int(vendedor[1])
    except:
        dic[vendedor[0]]=int(vendedor[1])
        vendedores.append(vendedor[0])

for i in vendedores:
    cant_vendedores.append(dic[i])

i = 0
while (i<len(vendedores)-1):
    k=i+1
    while (k<len(vendedores)):
        if cant_vendedores[i]<cant_vendedores[k]:
            temp = cant_vendedores[k]
            cant_vendedores[k] = cant_vendedores[i]
            cant_vendedores[i] = temp
            temp2 = vendedores[k]
            vendedores[k] = vendedores[i]
            vendedores[i] = temp2
            break
        k+=1

    i+=1


print("El vendedor del mes es "+vendedores[0])
