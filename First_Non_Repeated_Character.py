t=int(input())
while t:
    n=int(input())
    s=input()
    sum=0
    for i in range(len(s)):
        flag=0
        for j in range(len(s)):
            if(s[i]==s[j] and i!=j):
                flag=1
                break
        if flag==0:
            print(s[i])
            break
    if flag==1:
        print("-1")
    t-=1