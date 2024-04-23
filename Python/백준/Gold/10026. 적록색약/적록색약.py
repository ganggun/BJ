from collections import deque
import copy
def dfs(lst,i,j):
    q=deque()
    ck=[]
    ck.append([i,j])
    q.append([i,j])
    m=lst[i][j]
    lst[i][j]=0
    while q:
        p=q.popleft()
        for i in range(4):
            x=int(p[0]+dx[i])
            y=int(p[1]+dy[i])
            if x>=0 and x<n and y>=0 and y<n:
                if [x,y] not in ck and lst[x][y]==m :
                    q.append([x,y])
                    ck.append([x,y])
                    lst[x][y]=0


n=int(input())
lst=[]
for i in range(n):
    lst1=list(input())
    lst.append(lst1)
lst1=copy.deepcopy(lst)
dx=[0,1,0,-1]
dy=[1,0,-1,0]
p1=0
p2=0
for i in range(n):
    for j in range(n):
        if lst[i][j]!=0:
            dfs(lst,i,j)
            p1+=1
for i in range(n):
    for j in range(n):
        if lst1[i][j]=="G":
            lst1[i][j]="R"
for i in range(n):
    for j in range(n):
        if lst1[i][j]!=0:
            dfs(lst1,i,j)
            p2+=1
print(p1,p2)