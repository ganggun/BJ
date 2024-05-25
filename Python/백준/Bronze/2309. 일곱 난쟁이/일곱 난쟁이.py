lst=[]
for i in range(9):
    lst.append(int(input()))
n=sum(lst)
f=0
n=n-100
for i in range(9):
    if f==1:
        break
    for k in range(i+1,9):
        if f==1:
            break
        if lst[i]+lst[k]==n:
            lst[i]=0
            lst[k]=0
            
            f=1
lst.sort()
lst.pop(0)
lst.pop(0)
for i in lst:
    print(i)
