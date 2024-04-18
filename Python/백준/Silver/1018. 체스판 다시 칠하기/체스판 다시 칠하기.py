import copy as c
from collections import deque
def dfs(t):
    lst = c.deepcopy(lst1)
    lst[i][j] = t
    m = 0
    ck.clear()
    q.append([i, j])
    ck.append([i, j])
    while q:
        p = q.popleft()
        for k in range(4):
            x = p[0] + dx[k]
            y = p[1] + dy[k]
            if i <= x and i + 7 >= x and j <= y and j + 7 >= y and [x, y] not in ck:
                if lst[p[0]][p[1]] == "W":
                    if lst[x][y] != "B":
                        lst[x][y] = "B"
                        m += 1
                elif lst[p[0]][p[1]] == "B":
                    if lst[x][y] != "W":
                        lst[x][y] = "W"
                        m += 1
                ck.append([x, y])
                q.append([x, y])
    return m
a, b = map(int, input().split())
lst1 = []
ck = []
q = deque()
for i in range(a):
    lst1.append(list(input()))
dx=[-1,0,0,1]
dy=[0,-1,1,0]
mi=9*9
for i in range(a-7):
    for j in range(b-7):
        for s in range(2):
            if s==0:
                m=dfs("W")
                if lst1[i][j]!="W":
                    m+=1
            else:
                m=dfs("B")
                if lst1[i][j]!="B":
                    m+=1
            if mi>m:
                mi=m
print(mi)