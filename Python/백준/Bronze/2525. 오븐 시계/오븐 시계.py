n,m=map(int,input().split())
a=int(input())
p=n*60+m+a
p1=p//60
p2=p%60
print(p1%24,p2)