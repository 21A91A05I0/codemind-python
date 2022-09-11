n=int(input())
while(n!=1 and n!=4):
    sum=0
    while n!=0:
        r=n%10
        sum=sum+r*r
        n=n//10
    n=sum
if sum==1:
    print("True")
else:
    print("False")