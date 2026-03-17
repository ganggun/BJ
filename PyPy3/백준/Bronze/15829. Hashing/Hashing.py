n = int(input())
s=[ord(c)-ord('a')+1 for c in input()]
m=0
for i in range(n):
    m+=s[i]*(31**i)

print(int(m%1234567891))