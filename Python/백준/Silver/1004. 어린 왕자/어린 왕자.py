import math
a1=int(input())
for i in range(a1):
    n,m,n1,m1=map(int,input().split())
    a2=int(input())
    g=0
    for k in range(a2):
        x,y,r=map(int,input().split())
        if r>math.sqrt((x-n)**2+(y-m)**2)and r>math.sqrt((x-n1)**2+(y-m1)**2):
            g+=0
        elif r > math.sqrt((x - n) ** 2 + (y - m) ** 2) or r > math.sqrt((x - n1) ** 2 + (y - m1) ** 2):
            g+=1
    print(g)
