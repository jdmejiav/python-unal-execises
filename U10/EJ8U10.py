n = int (input())


mes_dic = {
    "enero":13,
    "febrero":14,
    "marzo":3,
    "abril":4,
    "mayo":5,
    "junio":6,
    "julio":7,
    "agosto":8,
    "septiembre":9,
    "octubre":10,
    "noviembre":11,
    "diciembre":12,
}
salida = []
day = {
    0:"sabado",
    1:"domingo",
    2:"lunes",
    3:"martes",
    4:"miercoles",
    5:"jueves",
    6:"viernes"
}

for i in range(0,n):
    entrada = input()
    dia_ent = entrada.split("-")
    mes = mes_dic[dia_ent[1]]
    dia = int(dia_ent[0])
    year = 0
    if mes == 13 or mes == 14:
        year = int(dia_ent[2])-1
    else:
        year = int(dia_ent[2])
    dia_sem = (dia + int((13*(mes+1)/5)) + year + int(year/4)-int(year/100)+int(year/400))%7

    print(day[int(dia_sem)])
