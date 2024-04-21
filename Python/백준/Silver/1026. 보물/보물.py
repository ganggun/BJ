a=int(input())
lst=list(map(int,input().split()))
lst1=list(map(int,input().split()))
lst.sort()
lst1.sort(reverse=True)
s=0
for i in range(a):
    s+=lst[i]*lst1[i]
print(s)