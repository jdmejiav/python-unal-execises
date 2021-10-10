n = int(input())



for i in range (0,n):
    dic1 = {}
    dic2 = {}

    entrada = input().lower()
    palabas = entrada.replace(' ','').split(":")
    palabra1 = palabas[0]
    palabra2 = palabas[1]
    for i in palabra1:
        if i in dic1:
            dic1[i]+=1
        else:
            dic1[i]=1
    for i in palabra2:
        if i in dic2:
            dic2[i]+=1
        else:
            dic2[i]=1

    anagrama=True
    for k in dic1.keys():
        if k not in dic2:
            anagrama=False
            break
        if dic1[k]!=dic2[k]:
            anagrama=False
            break
    for k in dic2.keys():
        if k not in dic1:
            anagrama=False
            break
        if dic1[k]!=dic2[k]:
            anagrama=False
            break

    if anagrama:
        print("Es anagrama")
    else:
        print("No es anagrama")
