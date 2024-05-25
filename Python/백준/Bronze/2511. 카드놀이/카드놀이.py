A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=0
b=0
c=0
for i in range(10):
    if (A[i])>(B[i]):
        a+=3
        c=1
    elif (A[i]) <(B[i]):
        b+=3
        c=2
    elif (A[i])==(B[i]):
        a+=1
        b+=1
if a>b:
    print(a,end=" ")
    print(b)
    print("A")
elif a<b:
    print(a,end=" ")
    print(b)
    print("B")
elif a==b:
    if c==1:
        print(a, end=" ")
        print(b)
        print("A")
    elif c==2:
        print(a, end=" ")
        print(b)
        print("B")
    else:
        print(a, end=" ")
        print(b)
        print("D")