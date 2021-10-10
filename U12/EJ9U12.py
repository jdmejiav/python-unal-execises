from datetime import datetime,timedelta
k = int (input())

for _ in range (0,k):
    deltas = []
    entrada = input()
    temp = entrada.split(',')
    nombre = temp[0]
    n = int(temp[1].replace(' ',''))
    past=None
    for i in range (0,n):
        entrada= input()
        if i == 0:
            past = datetime.strptime(entrada,"%Y-%m-%d")
        else:
            actual = datetime.strptime(entrada,"%Y-%m-%d")
            deltas.append(actual-past)
            past=actual

    dias = deltas[0].days
    periodico = True
    for i in range(1,n-1):
        if deltas[i].days != dias:
            periodico=False
    if periodico:
        prox = past+timedelta(days=dias)
        imp=prox.strftime("%Y-%m-%d")

        print(nombre+" ataca cada "+str(dias)+" dias y volvera a hacerlo en "+imp)
    else:
        print(nombre+" no es asesino(a) serial periodico")
    print()
