n=int(input())
i=n
j=0
while(n!=1):
    if(n%2==0):
        n=n//2
    elif(n%3==0):
        n=n/3
    elif n%5==0:
        n=n/5
    else:
        print("Not Ugly Number")
        j=1
        break
if j==0:
    print("Ugly Number")