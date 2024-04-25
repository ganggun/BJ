from collections import deque
def bfs(lstp):
    q=deque()
    for ii in lstp:
        q.append(ii)
    while q:
        p=q.popleft()
        for i in range(6):
            x=dx[i]+p[2]
            y=dy[i]+p[1]
            z=dz[i]+p[0]
            if 0 <= x < a and 0 <= y < b and 0 <= z < c:
                if lst[z][y][x] ==0:
                    lst[z][y][x]=lst[p[0]][p[1]][p[2]]+1
                    q.append((z,y,x))



a,b,c=map(int,input().split())
lst=[]
for j in range(c):
    lst1 = []
    for i in range(b):
        lst1.append(list(map(int,input().split())))
    lst.append(lst1)
dx=[0,1,0,-1,0,0]
dy=[1,0,-1,0,0,0]
dz=[0,0,0,0,-1,1]
lstp=[]
for i in range(c):
    for j in range(b):
        for k in range(a):
            if lst[i][j][k]==1:
                lstp.append((i,j,k))
bfs(lstp)
f=0
d=0

for i in range(c):
    for j in range(b):
        for k in range(a):
            if lst[i][j][k]==0:
                f=1
            if lst[i][j][k]>d:
                d=lst[i][j][k]
if f==1:
    print(-1)
else:print(d-1)