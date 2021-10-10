reggaeton= {}
rock={}
count_reggaeton = 0
count_rock = 0

n = int(input())
for i in range(0,n):
    entrada = input()
    ent_temp = entrada.split()
    for palabra in ent_temp:
        try:
            if reggaeton[palabra]:
                continue
        except:

            reggaeton[palabra] = True
            count_reggaeton+=1


n = int(input())
for i in range(0,n):
    entrada = input()
    ent_temp = entrada.split()
    for palabra in ent_temp:
        try:
            if rock[palabra]:
                continue
        except:
            rock[palabra] = True
            count_rock+=1

print("Reggaeton: "+str(count_reggaeton) +" Rock: "+str(count_rock))
