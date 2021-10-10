
archivo = open('mensaje.txt', 'r')
for renglon in archivo:
    print(renglon[::-1].replace('\n',''))
archivo.close()
