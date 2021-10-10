import calendar

n=int(input())



for i in range (0,n):
    entrada = input()
    fecha = entrada.split("/")
    calendario = calendar.Calendar().monthdayscalendar(int(fecha[2]),int(fecha[1]))
    print("lun\tmar\tmie\tjue\tvie\tsab\tdom")
    for sem in calendario:
        salidaSem = ""
        for dia in sem:
            if dia == 0:
                salidaSem+='\t'
            else:
                salidaSem+=str(dia)+'\t'

        print(salidaSem[:len(salidaSem)-1])
    print()
