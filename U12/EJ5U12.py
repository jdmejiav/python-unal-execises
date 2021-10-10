def limpiar(p):
    p=p.lower()
    p=p.strip('-')
    p=p.strip('"')
    p=p.lstrip('¿')
    p=p.lstrip('¡')
    p=p.rstrip('?')
    p=p.rstrip('!')
    p=p.rstrip(',')
    p=p.rstrip('.')
    p=p.rstrip(';')
    p=p.rstrip(':')
    return p



archivo = open('discurso.txt')
frecs = {}

maxFrec=0
for renglon in archivo:
    palabra=renglon.split()
    palabrasReng=[]
    for palabra in palabra:
        palabra = limpiar(palabra)
        if palabra not in frecs and len(palabra)>4:
            frecs[palabra]=1
            palabrasReng.append(palabra)
        else:
            if len(palabra)>4 and palabra not in palabrasReng:
                palabrasReng.append(palabra)
                frecs[palabra]+=1


for k in sorted(frecs):
    print(k+" "+str(frecs[k]))
