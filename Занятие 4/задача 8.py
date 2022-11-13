def count(n):
    n = int(input())
    k=i=1
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print(j, sep='', end='')
        print('')
count(n)
