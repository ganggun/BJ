def st(n):
    if n==3:
        for i in range(3):
            if i==1:
                lst[i][:3]=[1,0,1]
            else:
                lst[i][:3]=[1,1,1]
        return
    n//=3
    st(n)
    for j in range(3):
        for k in range(3):
            if (j,k) !=(1,1) and (j,k)!=(0,0):
                for ii in range(n):
                    lst[ii+(j*n)][n*k:n*(k+1)]=lst[ii][:n]
a=int(input())
lst=[[0 for i in range(a)]for j in range(a)]
st(a)
for i in range(a):
    for j in range(a):
        if lst[i][j]:
            print("*",end="")
        else:
            print(" ",end="")
    print()