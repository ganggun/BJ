import sys
sys.setrecursionlimit(10**6)
def dfs(lst,st,ck=None):
    if ck is None:
        ck=set()
    ck.add(st)
    for i in lst[st]:
        if i not in ck:
            plst[i]=st
            dfs(lst,i,ck)
a=int(input())
plst=[0]*(a+1)
lst=[[]for i in range(a+1)]
for i in range(a-1):
    n,m=map(int,input().split())
    lst[n].append(m)
    lst[m].append(n)
dfs(lst,1)
for i in plst[2:]:
    print(i)