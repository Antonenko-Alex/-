pol = 0
s = 0
N = 0
A = []
file = open("Антонеко Александр Валеревич_228_vvod.txt", 'r')
for line in file:
    a = list(map(int,line.split(' ')))
    A.append(a)
file.close()  
N = len(A)


for i in range(N):
    for j in range(i+1, N):
        if A[i][j] <= 0:
           continue
        if A[i][j] > 0:
            pol += 1
            s += A[i][j]

file = open("Антонеко Александр Валеревич_228_vivod.txt","w+")
file.write(str(s) + ' ' + str(pol))
file.close()
