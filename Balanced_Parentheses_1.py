s=input()
i=0
count=0
c=0
for i in range(len(s)):
    if s[i]=='(':
        count=count+1
    elif s[i]==')':
        c=c+1
if c==count:
    print("True")
else:
    print("False")