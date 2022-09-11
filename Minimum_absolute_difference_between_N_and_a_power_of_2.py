n=int(input())
from math import floor,log2
left=pow(2,floor(log2(n)))
right=left*2
d1=n-left
d2=right-n
if d1<d2:
    print(d1)
else:
    print(d2)