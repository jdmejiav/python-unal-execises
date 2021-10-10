n = int(input())
opinion = []


for k in range(0,n):
    entrada = input()
    if "positiva" in entrada:
        temp = (entrada.split())
        temp[2]="POSITIVA"
        opinion.append(temp[1:4])
opinion.sort(key=lambda x: (int(x[2]),int(x[0])))


for i in range(0,len(opinion)):
    print(opinion[len(opinion)-1-i][0]+" "+opinion[len(opinion)-1-i][1]+" "+opinion[len(opinion)-1-i][2])
