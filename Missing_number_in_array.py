t=int(input())
while t:
    n=int(input())
    sum=0
    a=list(map(int,input().split()))
    for i in range(len(a)):
        sum=sum+a[i]
    m=(n*(n+1))//2-sum
    print(m)
    t-=1