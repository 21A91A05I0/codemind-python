n=int(input())
a=list(map(int,input().split()))
large=0
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count+=1
    if count>large:
        large=count
        large1=a[i]
    if count==large:
        if(large1>a[i]):
            large1=a[i]
print(large1)        