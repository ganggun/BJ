lst=[list(input()) for i in range(5)]
l=0
for i in range(5):
    l=max(len(lst[i]),l)

for i in range(5):
    for j in range(l-len(lst[i])):
        lst[i].append("")

for i in range(l):
    for j in range(5):
        print(lst[j][i], end="")