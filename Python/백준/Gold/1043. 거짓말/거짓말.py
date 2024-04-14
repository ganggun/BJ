from collections import deque
n,m=map(int,input().split())
know=list(map(int,input().split()))
know.pop(0)
lst=[]
ck=0
c=[0 for i in range(n+1)]
for i in know:
    c[i]=1
for i in range(m):
    lst1=list(map(int,input().split()))
    lst1.pop(0)
    lst.append(lst1)
q=deque()
for i in know :
    q.append(i)
while q:
    p=q.popleft()
    for i in range(len(lst)):
        if p in lst[i]:
            for k in range(len(lst[i])):
                if c[lst[i][k]]!=1:
                    q.append(lst[i][k])
                    c[lst[i][k]]=1
            lst[i]=[-1]
            ck+=1
print(m-ck)
