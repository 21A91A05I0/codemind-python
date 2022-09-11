s=input()
a=[]
sum=0
for i in range(len(s)):
    if(s[i]=='M'):
        a.append(1000)
    if(s[i]=='D'):
        a.append(500)
    if(s[i]=='C'):
        a.append(100)
    if(s[i]=='L'):
        a.append(50)
    if(s[i]=='X'):
        a.append(10)
    if(s[i]=='V'):
        a.append(5)
    if(s[i]=='I'):
        a.append(1)
for i in range(len(a)):
    if i==len(a)-1 or a[i]>=a[i+1]:
        sum=sum+a[i]
    else:
        sum=sum-a[i]
print(sum)