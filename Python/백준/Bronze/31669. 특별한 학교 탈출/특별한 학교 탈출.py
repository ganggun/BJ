a,b=map(int,input().split())
lst=[]
c=0
for i in range(a):
    lst1=list(input())
    lst.append(lst1)
for i in range(b):
    f=0
    for j in range(a):
        if lst[j][i]=="O":
            f=1
    if f==0:
        print(i+1)
        c=1
        break
if c==0:
    print("ESCAPE FAILED")