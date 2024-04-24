from collections import deque
from sys import stdin
def bfs(k):
    q = deque()
    for ii in k:
        q.append(ii)
    while q:
        p=q.popleft()
        for i in range(4):
            x=p[0]+dx[i]
            y=p[1]+dy[i]
            if 0 <= x < b and 0<= y < a:
                if lst[x][y]==0:
                    if lst[x][y]>lst[p[0]][p[1]] or lst[x][y]==0:
                        f=1
                        lst[x][y]=lst[p[0]][p[1]]+1
                        q.append((x,y))


dx=[0,1,0,-1]
dy=[1,0,-1,0]
a,b=map(int, stdin.readline().split())
lst=[]
plst=[]
for i in range(b):
    lst.append(list(map(int, stdin.readline().split())))
f=0
for i in range(b):
    for j in range(a):
        if lst[i][j]==1:
            plst.append((i,j))
            # print(lst[i][j],i,j)
            # for i in range(b):
            #     for j in range(a):
            #         print(lst[i][j],end=" ")
            #     print()
            # print()
            # print()
#전체 탐색 조지고 0있으면 -1
bfs(plst)
mi=0
f1=0
for i in range(b):
    for j in range(a):
        if lst[i][j]==0:
            f1=1
        if lst[i][j]>mi:
            mi=lst[i][j]

if f==1:
    print(0)
elif f1==1:
    print(-1)
else:
    print(mi-1)