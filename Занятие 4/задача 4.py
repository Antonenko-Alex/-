def count(N):
    N = int(input())
    sum = 0
    for i in range(N, 0, -1):
        sum += int(input())
        print(sum)
count(N)
