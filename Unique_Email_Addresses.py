t=int(input())
a=[]
while t:
    t-=1
    a.append(input())
s=set()
for i in a:
    emailid=i.split("@")
    domain=emailid[1]
    e1=emailid[0].split("+")
    e2=e1[0].split(".")
    s.add("".join(e2)+"@"+domain)
print(len(s))