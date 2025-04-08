a=int(input())
lst=[]
for i in range(a):
    a,g=map(str,input().split())
    lst.append((int(a),g))
lst.sort(key=lambda x:x[0])
for i in lst:
    print(*i)
