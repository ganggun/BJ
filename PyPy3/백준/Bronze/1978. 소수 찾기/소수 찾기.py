def s(n):
    f=0
    if n==1:
        return 0
    if n==2:
        return 1
    for i in range(3,n,2):
        if n%i==0:
            f=1
    if f==1:
        return 0
    elif n%2==0:
        return 0
    else:
        return 1
a=int(input())
lst=list(map(int,input().split()))
p=0
for i in lst:
    p+=s(i)
print(p)