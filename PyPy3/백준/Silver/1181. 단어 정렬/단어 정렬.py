a=int(input())
lst=[]
for i in range(a):
    a=input()
    lst.append(a)
lst=set(lst)
lst=list(lst)
lst.sort(key=lambda x:(len(x),x))
for i in lst:
    print(i)

