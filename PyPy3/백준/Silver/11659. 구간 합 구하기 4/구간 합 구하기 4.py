n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst1=[0]*(n+1)
for i in range(len(lst)):
    lst1[i+1]=lst1[i]+lst[i]

for i in range(m):
    a,b=map(int,input().split())
    print(lst1[b]-lst1[a-1])