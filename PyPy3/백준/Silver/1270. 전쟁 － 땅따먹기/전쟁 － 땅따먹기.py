from sys import stdin
def re(lst):
    c=0
    n=0
    for i in lst:
        if c==0:
            n=i
        if i==n:
            c+=1
        else:
            c-=1
    if len(lst)//2<lst.count(n):
        return n
    else:return "SYJKGW"


n=int(stdin.readline())
for i in range(n):
    rlst=stdin.readline().split()
    rlst.pop(0)
    print(re(rlst))

