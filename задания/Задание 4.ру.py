a =int(input())
b =int(input())
if (a<=b):
    for i in(a,b+1):
        print(i, sep='')
else:
    for i in(a,b-1,a+1):
        print(a-i, sep='')

def count(a, b):
    if a<b:
        count(a, b - 1)
        print (b)
    elif a>b:
        print (a)
        count(a - 1, b)
a = input()
b = input()
count (a, b)

a = int(input())
b = int(input())
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end='')

N = int(input())
sum = 0
for i in range(N, 0, -1):
    sum += int(input())
print(sum)

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i**3
print(sum)

result = 1
n = int(input())
for i in range(1, n + 1):
    result *= i
print(result)

n = int(input())
f = 1
sum = 0
for i in range(1, n + 1):
    f = f * i
    sum += f
print(sum)

n = int(input())
k=i=1
for i in range(1, n+1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print('')

def Fib(n):
   if n==1 or n==2:
       return 1
   else:
       return Fib(n-2)+ Fib(n-1)
n=int(input("n="))
print(Fib(n+2)-1)

