a=int(input())
lst=list(map(int,input().split()))
n,m=map(int,input().split())
k=0
for i in range(6):
    if lst[i]%n==0:
        k += (lst[i] // n)
    else:
        k+=(lst[i]//n)+1
print(k)
print(a//m,a%m)