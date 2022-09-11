sum=0
count=0
p=0
q=0
a,n=map(int,input().split())
temp=a
while(temp!=0):
    m=temp%10
    p=p*10+m
    temp=temp//10
for i in range(n):
    r=a%10
    sum=sum*10+r
    a=a//10
for i in range(n):
    s=sum%10
    count=count*10+s
    sum=sum//10
    
for i in range(n):
    j=p%10
    q=q*10+j
    p=p//10
diff=abs(count-q)
print("%d"%diff)