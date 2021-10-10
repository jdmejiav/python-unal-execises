
n = int(input())
dic ={}

for i in range(0,n):
    entrada = input()
    ent = entrada.split()
    dic[ent[0]] = ent[1]

n = int(input())

for i in range (0,n):
    try:
        entrada = input()
        print(dic[entrada])
    except:
        print("palabra no encontrada")
