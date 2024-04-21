from collections import deque
def bfs(x,y):
    q = deque()
    q.append([x,y])
    lst[x][y]=0
    while q:
        d=q.popleft()
        for i in range(4):
            dx=d[0]+x1[i]
            dy=d[1]+y1[i]
            if b>dx>=0 and a>dy>=0:
                if lst[dx][dy]==1:
                    q.append([dx,dy])
                    lst[dx][dy]=0
p=0

x1 = [1,-1,0,0]
y1 = [0,0,1,-1]
a=int(input())
for iaa in range(a):
    a,b,c=map(int,input().split())
    lst=[]
    for i1 in range(b):
        lst1=[0]*a
        lst.append(lst1)
    for o in range(c):
        u,i=map(int,input().split())
        lst[i][u]=1

    for i in range(b):
        for j in range(a):
            if lst[i][j]==1:
                bfs(i,j)
                p+=1
    print(p)
    p = 0
