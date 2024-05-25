l=list(input())
n=int(input())
r=[]
for i in range(n):
    lst=input()
    if lst[0]=="P":
        l.append(lst[2])
    elif lst[0]=="D":
        if len(r)==0:
            continue
        else:
            r1=r.pop()
            l.append(r1)
    elif lst[0]=="L":
        if len(l)==0:
            continue
        else:
            l1=l.pop()
            r.append(l1)
    elif lst[0]=="B":
        if len(l)==0:
            continue
        else:
            l.pop()
r.reverse()

p=l+r
for i in p:
    print(i,end="")