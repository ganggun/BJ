n,m=map(int,input().split())
lst=[0 for _ in range(m+1)]
lst[1]=1
i=0
while True:
    if lst[i+1] == 0:
        for k in range(0,m+1,i+1):
            lst[k]=1
        if n<=i+1:
            print(i+1)
    i+=1
    if i==m:
        break
