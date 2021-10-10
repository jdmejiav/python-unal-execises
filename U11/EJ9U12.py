from datetime import timedelta, datetime

n = int(input())



for _ in range (0,n):
    entrada = input()
    fecha = datetime.strptime(entrada,'%d/%m/%Y')

    mes = fecha.month
    fechaIt = datetime(fecha.year,fecha.month,1)
    salida=""
    print("lun\tmar\tmie\tjue\tvie\tsab\tdom")

    for i in range(0,fechaIt.weekday()):
        salida+='\t'

    while fechaIt.month == mes:
        salida+=str(fechaIt.day)
        if fechaIt.weekday() == 6:
            salida+="\n"
        else:
            salida+="\t"
        fechaIt=fechaIt+timedelta(1)
        
    if fechaIt.weekday()==0:
        print(salida)
    else:
        print(salida+"\n")
    salida=""
