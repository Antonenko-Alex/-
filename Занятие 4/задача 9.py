def Fib(n):
   if n==1 or n==2:
       return 1
   else:
       return Fib(n-2)+ Fib(n-1)
n=int(input("n="))
print(Fib(n+2)-1)
