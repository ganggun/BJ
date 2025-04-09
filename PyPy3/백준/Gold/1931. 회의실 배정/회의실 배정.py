a=int(input())
lst=[]
for i in range(a):
    lst.append(list(map(int,input().split())))
lst.sort(key=lambda x:(x[1],x[0]))
e=0
c=0
for i in range(len(lst)):
    if lst[i][0]>=e:
        c+=1
        e=lst[i][1]
print(c)