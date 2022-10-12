def vowel(s):
    if s in 'aeiouAEIOU':
        return 1
    else:
        return 0
s=input()
a=[]
c=0
j=0
k=-1
for i in range(len(s)):
    if s[i]==' ':
        a.append(i)
for i in range(len(s)):
    if vowel(s[k+1]) and (not(vowel(s[a[j]-1]))):
        c+=1
    j+=1
    if j<len(a):
        k=a[j-1]
    else:
        break
if vowel(s[a[j-1]+1]) and (not(vowel(s[len(s)-1]))):
    c+=1
print(c)