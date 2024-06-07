lst=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
a=input()
p=0
for j in a:
    for i in range(len(lst)):
        if j in lst[i]:
            p+=i+3
print(p)