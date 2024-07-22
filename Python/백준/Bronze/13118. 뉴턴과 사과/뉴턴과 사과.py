lst=list(map(int,input().split()))
a,b,c=map(int,input().split())
if a not in lst:
    print(0)
else:
    print(lst.index(a)+1)
