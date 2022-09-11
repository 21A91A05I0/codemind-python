s=input()
t=input()
s1=[]
for i in s:
    if i!='#':
        s1.append(i)
    else:
        if len(s1)>0:
            s1.pop()
t1=[]
for i in t:
    if(i!='#'):
        t1.append(i)
    else:
        if(len(t1)>0):
            t1.pop()
if(s1==t1):
    print("True")
else:
    print("False")