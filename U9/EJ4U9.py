

n = int(input())
salida = []
for j in range(0,n):
    entrada = input()
    entrada_separada=entrada.split()
    mio = entrada_separada[0]
    esmenor=False
    flag = False
    for k in range (1,len(entrada_separada)):

        for i in range(0,6):

            if ord(mio[i]) < ord(entrada_separada[k][i]):
                esmayor=True
                break
            elif ord(mio[i]) > ord(entrada_separada[k][i]):
                esmayor=False
                flag =True
                break
        if flag:
            break
            
    if esmayor:
        salida.append("Mi cacharrito es el mas viejo de todos los autos ;D")
        esmenor=False
    else:
        salida.append("Al menos otro auto es mas viejo que mi cacharrito :(")
        esmenor=False

for i in salida:
    print(i)
