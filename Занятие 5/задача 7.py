def count(i):
    i = int(input())
    a = 0
    b = 0
    k=i
    while i !=0:
        i = int(input())
        if i>k:
            b+=1
        k=i
    print(b)
count(i)
