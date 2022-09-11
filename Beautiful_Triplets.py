n=int(input())
s=list(map(int,input().split()))
s.sort(reverse=True)
while s:
    print(len(s))
    min=s.pop()
    while s and min==s[-1]:
        s.pop()