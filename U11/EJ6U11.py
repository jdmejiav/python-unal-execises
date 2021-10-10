from datetime import datetime


n = int(input())

for i in range(0,n):
    entrada = input().split()
    edad = int(entrada[1])
    date = datetime.strptime(entrada[0], '%Y/%m/%d')
    lunes = 0
    for i in range (date.year+1,date.year+edad+1):
        temp = datetime(i,date.month,date.day)
        if temp.weekday()==0:
            lunes += 1

    print(lunes)
