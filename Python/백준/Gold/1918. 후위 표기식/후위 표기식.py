def pr(op):
    if op =="(" or op ==")":return 0
    elif op =="+" or op =="-":return 1
    elif op == "*" or op == "/": return 2
    else:
        return -1
lst=list(map(str,input()))
s=[]
p=[]
for i in lst:
    if i =="(":
        s.append("(")
    elif i ==")":
        while not len(s)==0:
            op =s.pop()
            if op == "(":
                break
            else:
                p.append(op)
    elif i in "+-*/":
        while not len(s)==0:
            op = s[-1]
            if pr(i)<= pr(op ):
                p.append(op)
                s.pop()
            else:
                break
        s.append(i)
    else:
        p.append(i)
while len(s)!=0:
    p.append(s.pop())
for i in p:
    print(i,end="")
