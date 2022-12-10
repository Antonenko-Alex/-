l=[]
def f(l):
    n=int(input('Введите число: '))
    if n == 0:
        return l
    l.append(n)
    return f(l)


l=f(l)
l.sort()
print('Второе максимальное число: ',l[-2])