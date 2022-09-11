n=int(input())
a=[]
b=[]
c=0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    b.append(int(input()))
for i in range(n):
    for j in range(n):
        if a[i]<=b[j]:
            c+=1
            b[j]=-1
            break
print(abs(n-c))