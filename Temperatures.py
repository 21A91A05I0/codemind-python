n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    flag=0
    for j in range(i+1,n):
        if(a[j]>a[i]):
            print(j-i,end=" ")
            flag=1
            break
    if flag==0:
        print("0",end=" ")