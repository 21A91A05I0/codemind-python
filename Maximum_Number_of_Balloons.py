s=input()
ans=0
b=0
a=0
l=0
o=0
n=0
for i in range(len(s)):
    if(s[i]=='b'):
        b+=1
    if(s[i]=='a'):
        a+=1
    if(s[i]=="l"):
        l+=1
    if(s[i]=="o"):
        o+=1
    if(s[i]=="n"):
        n+=1
    if(b>=1 and a>=1 and l>=2 and o>=2 and n>=1):
        ans+=1
        b-=1
        a-=1
        l-=2
        o-=2
        n-=1
print(ans)