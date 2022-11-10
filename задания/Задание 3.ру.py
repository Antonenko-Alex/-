a = int(input())
b = int(input())
c = int(input())
s=a+b+c
print(s)

a = int(input())
b =int(input())
print(1/2 * a * b)

n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)

a = int(input())
a = int(input())
L = int(input())
N = int(input())
print(2 * L + (2*N-1)*a+2*(N-1)*b)

a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else: 
    print(0)
