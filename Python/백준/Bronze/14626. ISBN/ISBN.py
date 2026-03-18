lst=list(input())
a=0
f=3
for i in range(len(lst)-1):
    if lst[i]=="*":
        if i%2==0:
            f=1
    elif i%2==0:
        a+=int(lst[i])
    else:
        a+=int(lst[i])*3
    # print(lst[i],a)
for i in range(10):
    if (10-((a+i*f)%10))%10== int(lst[-1]):
        print(i)
        # if i==0:
        #     print(0)
        # else:
        #     if lst[-1]== "0":
        #         print(i)
        #     else:
        #         print(10-i)
# print('\n'.join(lst))