n=int(input())
k=int(input())
a=[]
c=0
max=0
while(n!=0):
    r=n%k
    a.append(r)
    n=n//k
for i in range(0,len(a)):
    if a[i]==0:
        c+=1
    else:
        if c>max:
            max=c
        c=0
if max>0:
    print(max)
else:
    print("-1")