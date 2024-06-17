from collections import deque
def bfs(lst,s):
    clst=[0 for _ in range(a+1)]
    clst[s]=1
    q=deque()
    q.append(s)
    lst[s].sort()
    rlst=[s]
    while q:
        p=q.popleft()
        lst[p].sort()

        for i in lst[p]:
            if not clst[i]:
                clst[i]=1
                rlst.append(i)
                q.append(i)
    return rlst
def dfs(lst,s):
    cset=set()
    cset.add(s)
    st=[]
    st.append(s)
    lst[s].sort(reverse=True)
    rlst=[s]
    while st:
        p=st.pop()
        lst[p].sort(reverse=True)
        if p not in cset:
            cset.add(p)

            rlst.append(p)
        for i in lst[p]:
            if i not in cset:
                st.append(i)
    return rlst
a,b,c=map(int,input().split())
lst=[[] for i in range(a+1)]
for i in range(b):
    n,m=map(int,input().split())
    lst[n].append(m)
    lst[m].append(n)
print(*dfs(lst,c))
print(*bfs(lst,c))