lst=[-1 for i in range(26)]
a=input()
for i in range(len(a)):
    b=lst[ord(a[i])-97]
    if b ==-1:
        lst[ord(a[i])-97]=i
print(*lst)