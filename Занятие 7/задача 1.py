def tesk1(n):
  n = int(input())
  a = list(map(int, input().split()))
  m = max(a)
  a.reverse()
  print(m)
  print(*a)
tesk1(n)
