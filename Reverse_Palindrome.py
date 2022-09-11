n=int(input())
for i in range(100):
    t=n
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    n=s+t
    t=n
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    if s==t:
        print(s)
        break
    else:
        n=s+t
        t=n
        s=0