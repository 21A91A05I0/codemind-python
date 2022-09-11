t=int(input())
while t:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    flag=0
    s,k=0,0
    for i in range(0,n):
        s,k=0,0
        s=sum(a[:i])
        k=sum(a[i+1:])
        if s==k:
            flag=1
            break
    if flag==1:
        print("YES")
    else:
        print("NO")
    