r,m=map(str,input().split())
c=0
m1=[]
for i in m:
    m1.append(i)
for i in r:
    if i in m1:
        m1.remove(i)
        continue
    else:
        print("False")
        c+=1
        break
if(c==0):
    print("True")