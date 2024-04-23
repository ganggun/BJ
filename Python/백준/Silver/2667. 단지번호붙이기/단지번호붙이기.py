from collections import deque
import copy
def dfs(lst,i,j):
    q=deque()
    ck=[]
    ck.append([i,j])
    q.append([i,j])
    m=lst[i][j]
    lst[i][j]=0
    pl=0
    while q:
        p=q.popleft()
        for i in range(4):
            x=int(p[0]+dx[i])
            y=int(p[1]+dy[i])
            if x>=0 and x<n and y>=0 and y<n:
                if [x,y] not in ck and lst[x][y]==m :
                    q.append([x,y])
                    ck.append([x,y])
                    pl+=1
                    lst[x][y]="0"
    return pl


n=int(input())
lst=[]
for i in range(n):
    lst1=list(input())
    lst.append(lst1)
plst=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
p1=0
p2=0
for i in range(n):
    for j in range(n):
        if lst[i][j]!="0":
            plst.append(dfs(lst,i,j)+1)
            p1+=1
            # for ii in range(n):
            #     for jj in range(n):
            #         print(lst[ii][jj],end=" ")
            #     print()
            # print()
            # print()
print(p1)
plst.sort()
for i in plst:
    print(i)