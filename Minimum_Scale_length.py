n=int(input())
c=0
sum=0
a=list(map(int,input().split()))
for i in range(2,100):
    count=0
    for j in range(n):
        if(a[j]%i==0):
            count+=1
    if count==n:
        if i>sum:
            sum=i
if sum>0:
    print(sum)
else:
    print("1")