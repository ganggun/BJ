a,b=map(list,input().split())
a.reverse(),b.reverse()
print("".join(a)) if int("".join(a))>int("".join(b)) else print("".join(b))

