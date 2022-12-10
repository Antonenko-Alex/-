def f(z,x):
    if (z-x)<0:
        return z
    elif (z-x)==0:
        return 0
    else:
        return f((z-x),x)

a = int(input('Введите a: '))
b = int(input('Введите b: '))
print(f(a,b))
