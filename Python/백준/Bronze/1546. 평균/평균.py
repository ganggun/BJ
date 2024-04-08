a=int(input())
lst=list(map(int,input().split()))
m=max(lst)
for i in range(a):
    lst[i]=lst[i]/m*100
print(sum(lst)/len(lst))