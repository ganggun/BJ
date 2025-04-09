a,b=map(int,input().split())
m=0
for i in range(min(a,b)):
    if a%(i+1)==0 and b%(i+1)==0:
        m=i+1
print(m)
p=max(a,b)
while True:
    if p%b==0 and p%a==0:
        print(p)
        break
    p+=m
