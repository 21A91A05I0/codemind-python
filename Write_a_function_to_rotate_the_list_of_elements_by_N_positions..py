n=int(input())
a=list(map(int,input().split()))
k=int(input())
for i in range(k):
    temp=a[n-1]
    for j in range(n-1,0,-1):
        a[j]=a[j-1]
    a[0]=temp
for i in range(n):
    print(a[i],end=" ")