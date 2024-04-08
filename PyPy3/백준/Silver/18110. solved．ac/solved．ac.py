import sys


def a1(p1):
    if p1%2<1 and p1%1==0.5:
        p1+=1
        p1=p1//1
        p1=int(p1)
        return p1
    return round(p1)
a=int(input())
lst=[0]*a
if a==0:
    print(0)
else:
    for i in range(a):
        lst[i]=int(sys.stdin.readline())
    m=a1(len(lst)*15/100)
    lst.sort()
    p=sum(lst[m:len(lst)-m])/len(lst[m:len(lst)-m])
    k=a1(p)
    print(k)