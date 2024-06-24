from sys import stdin
m=int(stdin.readline())
for i in range(m):
    n=int(stdin.readline())
    lst=[0 for _ in range(n+1)]
    for j in range(len(lst)-2):
        if j+1<n+1:
            lst[j+1]+=lst[j]+1
        if j + 2< n+1:
            lst[j + 2] += lst[j]+1
        if j + 3 < n+1:
            lst[j + 3] += lst[j]+1
    print(lst[n]+1)
