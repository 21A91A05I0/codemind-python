t=int(input())
while(t):
    t-=1
    D,d,p,q=map(int,input().split())
    k=0
    n=D//d
    r=D%d
    f=n/2
    k=d*(f*(2*p+(n-1)*q))
    if r!=0:
        k+=r*(p+(n*q))
    print("%.f"%k)