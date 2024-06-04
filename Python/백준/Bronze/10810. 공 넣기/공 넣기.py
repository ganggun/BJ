n,m=map(int,input().split())
lst=[0]*n
for i in range(m):
    a,b,c=map(int,input().split())
    d=abs(a-b)
    if d==0:
        lst[a-1] = c
    else:
        lst[a-1:b]=[c]*(abs(a-b)+1)
print(*lst)