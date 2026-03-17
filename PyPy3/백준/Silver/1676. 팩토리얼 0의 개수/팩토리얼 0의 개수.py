n=int(input())
s=1
for i in range(1,n+1):
    s*=i
lst=list(map(int,str(s)))
lst.reverse()
for i in range(len(lst)):
    if lst[i]!=0:
        print(i)
        break


