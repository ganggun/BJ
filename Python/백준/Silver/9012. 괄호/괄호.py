n=int(input())
for i in range(n):
    a=list(input())
    lst=[]
    f=0
    for j in a:
        if j=="(":
            lst.append(j)
        else:
            if len(lst)!=0 and lst[-1]=="(" :
                lst.pop()
            else:
                f=1
                break
    if f==1:
        print("NO")
    elif len(lst)!=0:
        print("NO")
    else:
        print("YES")