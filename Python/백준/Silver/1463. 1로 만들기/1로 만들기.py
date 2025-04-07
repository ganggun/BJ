
a=int(input())
lst=[0]*(a+1)
lst[1]=0
for i in range(2,a+1):
    lst[i]=lst[i-1]+1
    if lst[i]>lst[i//2]+1 and i%2==0:
        lst[i]=lst[i//2]+1
    if lst[i]>lst[i//3]+1 and i%3==0:
        lst[i]=lst[i//3]+1
print(lst[a])