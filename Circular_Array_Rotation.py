n,k,q=map(int,input().split())
a=tuple(map(int,input().split()))
for i in range(q):
    print(a[(int(input())+n-k)%n])