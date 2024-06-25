from collections import deque
n,m=map(int,input().split())
if n==m:
    print(0)
elif m<n:
    print(n-m)
else:
    lst=[0 for _ in range(m*2)]
    q=deque()
    q.append(n)
    while q:
        p=q.popleft()
        if 0<=p+1<m*2:
            if lst[p+1]==0 or lst[p +1] > lst[p]+1 :
                lst[p+1]=lst[p]+1
                q.append(p+1)
        if  0<=p-1<m*2:
            if lst[p -1] == 0 or lst[p -1] > lst[p]+1 :
                lst[p-1]=lst[p]+1
                q.append(p-1)
        if 0<=p*2<m*2 :
            if lst[p * 2] == 0 or  lst[p * 2]>lst[p]+1:
                lst[p*2]=lst[p]+1
                q.append(p*2)
        if lst[m]!=0:
            break
    print(lst[m])

