t=int(input())
while(t):
    s=input()
    c=0
    for i in range(1,len(s)):
        if(s[i]==s[i-1]):
            c+=1
    print(c)
    t-=1
