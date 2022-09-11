n=int(input())
for i in range(0,1<<n):
    for j in range(n-1,-1,-1):
        if(1<<j)&i>0:
            print("1",end="")
        else:
            print("0",end="")
    print()