lst,n=input().split()
n=int(n)
lst=list(lst)
lst.reverse()
p=0
for i in range (len(lst)):
    if lst[i].isdigit():
        p+=int(lst[i])*(n**i)
    else:
        p+=(ord(lst[i])-55)*(n**i)
print(p)