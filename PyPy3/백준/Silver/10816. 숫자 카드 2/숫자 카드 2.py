a=int(input())
lst=list(map(int,input().split()))
b=int(input())
d={}
lst1=list(map(int,input().split()))
for i in range(len(lst)):
    if lst[i] not in d:
        d[lst[i]]=1
    else:
        d[lst[i]]+=1
for i in range(len(lst1)):
    if lst1[i] not in d:
        print(0,end=" ")
    else:
        print(d[lst1[i]],end=" ")
