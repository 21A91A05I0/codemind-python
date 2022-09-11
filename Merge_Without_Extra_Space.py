t=int(input())
while t:
    n1,n2=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    n=len(a)
    k=len(b)
    c=[]
    for i in range(n1):
        c.append(a[i])
    for i in range(n2):
        c.append(b[i])
    c.sort()
    for i in range((n1+n2)-1):
        print(c[i],end=' ')
    print(c[(n1+n2)-1])
    t=t-1