

procedencia = {
    "ix":"Galo",
    "us":"Romano",
    "ic":"Godo",
    "as":"Griego",
    "af":"Normando",
    "is":"Breton",
    "ax":"Breton",
    "ez":"Hispano",
    "a":"Indio"
}


n = int(input())

if (n <= 5000):
    salida = []
    for i in range(0,n):

        entrada = input()

        try:
            salida.append(procedencia[entrada[len(entrada)-2:]])
        except:
            try:
                salida.append(procedencia[entrada[len(entrada)-1:]])
            except:
                salida.append("Desconocido")
    for i in salida:
        print(i)
