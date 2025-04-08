def a(s):
    if len(s)%2==0:
        lst=s[:len(s)//2]
        lst1 = s[len(s) // 2:]
    else:
        lst=s[:len(s)//2]
        lst1=s[(len(s)//2)+1:]
    lst=list(lst)
    lst.reverse()
    if lst==list(lst1):
        return "yes"
    else:
        return "no"
while True:
    n=input()
    if n=="0":
        break
    print(a(n))