lst=[0]*200
a=input()
for i in a:
    if ord(i)<97:
        lst[ord(i)+32]+=1
    else:
        lst[ord(i)]+=1
m=max(lst)
f=0
x=0
for i in range(len(lst)):
    if m==lst[i]:
        f+=1
        x=i
if f==1:
    print(chr(x-32))
else:
    print("?")