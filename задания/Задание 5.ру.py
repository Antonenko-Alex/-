n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1

n = int(input())
i = 2
while n % 1 !=0:
    i += 1
print(i)

N = int(input())
s = 1
i = -1
while s<=N:
    i+=1
    s*=2
print(i,s*0,5)

x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)


i = 0
while int(input()) != 0:
    i += 1
print(i)

x = int(input())
s = i = 0
while x !=0:
    s += x
    i += 1
    x = int(input())
print(s/1)

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

p = int(input())
c = 1
b = 0
while p!=0:
    v=int(input())
    p,v=v,p
    if v==p:
        c+=1
    if c>b:
        b=c
    if p!=v:
        c=1
print(b)        
