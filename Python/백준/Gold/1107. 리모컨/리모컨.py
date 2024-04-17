a=input()
b=int(input())
lst1=[]
g="0"
if b==0:
    pass
else:
    lst1=list(map(int,input().split()))
for i in range(len(lst1)):
    lst1[i]=int(lst1[i])
lst=[i for i in range(10)]
for i in range(len(lst1)):
    lst.pop(lst.index(lst1[i]))
if lst:
    pass
else:
    lst.append(0)
#print(lst)
lstp=[]
f=0
p=""
a=str(int(a))
for i in range(len(a)):
    if f==0:
        if int(a[i]) in lst:
            p+=a[i]
            g = a[i]
            #print(p)
        else:
            for j in range(10):
                if int(a[i])-j>0:
                    p1=p
                    p1+=str(j)
                    for _ in range(len(a)-len(p1)):
                        p1+=str(max(lst))
                    lstp.append(p1)
                    f=1
                else:
                    p1=p
                    p1+=str(j)
                    for _ in range(len(a)-len(p1)):
                        p1+=str(min(lst))
                    lstp.append(p1)
                    f=1
    else:
        break
p2=""
if p:
    p=list(p)
    p.pop()
    if p:
        for i in p:
            p2+=i
# print(p2)
# print(lstp,"slt 정렬")
if 0 in lst and len(lst)>1:
    lstp.append(str(lst[1])+str(min(lst))*(len(str(int(a)))))
else:
    lstp.append(str(lst[0]) * (len(str(int(a))) + 1))
    #print("Dddd")
if len(a)-1!=0:
    #print(len(str(int(a))),a)
    lstp.append(str(max(lst))*(len(a)-1))
#print(g)
g1=2147483647
k1=0
for i in range(len(lst)):
    if g1>abs(int(g)-lst[i]) and int(g)-lst[i]>0 and lst[i]!=0:
        k1=lst[i]
        g1=abs(int(g)-lst[i])
#print(k1,"k1")
lstp.append(p2+str(k1)+str(max(lst))*(len(a)-len(p)-1))
g1=2147483647
k2=0
for i in range(len(lst)):
    if g1>abs(int(g)-lst[i]) and int(g)-lst[i]<0 and lst[i]!=0:
        k2=lst[i]
        g1=abs(int(g)-lst[i])
#print(k2,"k2")
lstp.append(p2+str(k2)+str(min(lst))*(len(a)-len(p)-1))
k=0
m1=2147483647
m=0
#print(lstp,"lstp")
for i in range(len(lstp)):
    k=0
    for j in range(len(lst1)):
        if str(lst1[j]) in str(int(lstp[i])):
            k=1
    if k==0 and int(m1)>abs(int(a)-int(lstp[i])) :
        m=int(lstp[i])
        m1=abs(int(a)-int(lstp[i]))
        # print(m,"m")
    elif k==0 and int(m1)==abs(int(a)-int(lstp[i])):
        if len(str(m)) > len(str(int(lstp[i]))):
            m=int(lstp[i])
            m1=abs(int(m)-int(lstp[i]))
            # print(m,"m")
p1=len(str(m))+abs(int(a)-int(m))
# print(f,"f")
# print(p1,"p1")
if b==10:
    print(abs(100-int(a)))
elif f==0 and len(a)<abs(int(a)-100) :
    print(len(a))
elif abs(int(a)-100)<p1:
    print(abs(int(a)-100))
else:
    print(p1)

