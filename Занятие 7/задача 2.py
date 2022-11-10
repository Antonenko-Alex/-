a = list(map(float, input().split()))
av = sum(a) / len(a)
for i in range(len(a)):
    if a[i] == 0:
        a[i] = av
print(a[i], end=" ")
