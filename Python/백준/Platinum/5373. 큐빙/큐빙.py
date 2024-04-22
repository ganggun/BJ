from collections import deque
def minus(q):
    for ii in range(3):
        s1 = q.popleft()
        q.append(s1)
def pu(q):
    for ii in range(3):
        s1 = q.pop()
        q.appendleft(s1)

def so(n,m):
    st=[]
    for i in range(4):
        st1=[]
        for j in range(3):
            st1.append(m[i][dx[i][j]][dy[i][j]])
            m[i][dx[i][j]][dy[i][j]]=-1
        st+=st1
    st=deque(st)
    if n=="-":
        minus(st)
    elif n=="+":
        pu(st)
    g=0
    for i1 in range(4):
        for j1 in range(3):
            m[i1][dx[i1][j1]][dy[i1][j1]]=st[g]
            g+=1
    #면회전
def so1(m,n):
    st=deque()
    for i in range(8):
        st.append(m[mx[i]][my[i]])
    if n == "-":
        minus(st)
        k=st.pop()
        st.appendleft(k)
    elif n == "+":
        pu(st)
        k=st.popleft()
        st.append(k)
    for j in range(8):
        m[mx[j]][my[j]]=st[j]
def set(t):
    return [[t for i in range(3)] for j in range(3)]
a=int(input())
for i in range(a):
    wlst = set("w")
    ylst = set("y")
    rlst = set("r")
    olst = set("o")
    glst = set("g")
    blst = set("b")
    mx = [0, 1, 2, 2, 2, 1, 0, 0]
    my = [0, 0, 0, 1, 2, 2, 2, 1]
    dx = [[2, 2, 2], [2, 1, 0], [0, 1, 2], [0, 0, 0]]
    dy = [[2, 1, 0], [0, 0, 0], [2, 2, 2], [0, 1, 2]]
    u = [olst, blst, rlst, glst]
    u.reverse()
    d = u[:]
    u.reverse()
    f = [ylst, glst, wlst, blst]
    f.reverse()
    b = f[:]
    f.reverse()
    l = [rlst, ylst, olst, wlst]
    l.reverse()
    r = l[:]
    l.reverse()
    b1=int(input())
    n=list(map(str,input().split()))
    for j in range(b1):
        if n[j][0]=="L":
            so(n[j][1],l)
            so1(glst,n[j][1])
        elif n[j][0]=="U":
            so(n[j][1],u)
            so1(wlst,n[j][1])
        elif n[j][0]=="D":
            so(n[j][1],d)
            so1(ylst,n[j][1])
        elif n[j][0]=="F":
            so(n[j][1],f)
            so1(rlst,n[j][1])
        elif n[j][0]=="B":
            so(n[j][1],b)
            so1(olst,n[j][1])
        elif n[j][0]=="R":
            so(n[j][1],r)
            so1(blst,n[j][1])
    for ik in range(3):
        for jk in range(3):
            print(wlst[jk][ik],end="")
        print()