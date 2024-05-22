n,m=map(int,input().split())
lsta=[]
for i in range(n):
    lsta.append(list(map(int,input().split())))
lstb=[]
for i in range(n):
    lstb.append(list(map(int,input().split())))
lstc=[[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
    for j in range(m):
        lstc[i][j]=lsta[i][j]+lstb[i][j]
for i in range(n):
    for j in range(m):
        print(lstc[i][j],end=" ")
    print()