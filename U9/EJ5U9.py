
n = int(input())
salida = []

for i in range(0,n):
    entrada = input ()
    entrada=entrada.lower()
    vocales = 0
    if "a" in entrada or "á" in entrada:
        vocales+=1

    if "e" in entrada or "é" in entrada:
        vocales+=1

    if "i" in entrada or "í" in entrada:
        vocales+=1

    if "o" in entrada or "ó" in entrada:
        vocales+=1

    if "u" in entrada or "ú" in entrada:
        vocales+=1


    if vocales == 5:
        salida.append("Panvocalica")
    else:
        salida.append("No es panvocalica")

for i in salida:
    print(i)
