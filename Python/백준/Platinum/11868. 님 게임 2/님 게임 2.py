a=int(input())
lst=list(map(int,input().split()))
if len(list(filter(lambda x:x==1,lst)))==len(lst):
    if len(lst)%2==0:
        print("cubelover")
    else:
        print("koosaga")

else:
    if a==1:
        print("koosaga")
    elif a==2:
        print("cubelover") if lst[0]==lst[-1] else print("koosaga")
    else:
        c = lst.pop(0)
        for i in lst:
            c^=i
        if c==0:
            print("cubelover")

        else:
            print("koosaga")
