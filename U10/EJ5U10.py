m = int(input())

for i in range(0,m):

    n = int(input())
    bandera = True
    for i in range(0,n):
        temp = input()
        for j in range(0,n):
            if i==int(n/2):

                if j==int(n/2):
                    if temp[j]!='#':
                        bandera=False

                        break
                else:
                    if temp[j]!='+':
                        bandera=False

                        break
            else:
                if j == i or n-i-1 == j:
                    if temp[j] != '#':

                        bandera = False
                        break
                elif j==int(n/2):

                    if temp[j] != '+':

                        bandera=False
                        break
                elif temp[j] != '0':

                    bandera = False
                    break



    if bandera:
        print("Bandera britanica")
    else:
        print("Ni idea")
