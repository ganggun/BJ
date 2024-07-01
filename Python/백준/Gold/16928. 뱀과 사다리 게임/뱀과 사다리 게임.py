from collections import deque
g = [i for i in range(101)]
b = [0 for l in range(101)]
q=deque()
n,m = map(int,input().split())
for i in range(n+m):
    x,y = map(int,input().split())
    g[x] = y
q.append(1)
b[1]=0
while q:
    t=q.popleft()
    for i in range(1,7):
        if  t+i<=100 and b[t+i]==0 :
            q.append(g[t+i])
            b[t+i]=b[t]+1
            if b[g[t+i]]==0:
                b[g[t + i]]=b[t]+1
print(b[-1])



