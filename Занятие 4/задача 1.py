a =int(input())
b =int(input())
if (a<=b):
    for i in(a,b+1):
        print(i, sep='')
else:
    for i in(a,b-1,a+1):
        print(a-i, sep='')
