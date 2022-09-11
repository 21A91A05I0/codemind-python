def permute(s,k):
    if(len(s)==0):
        print(k)
        return
    for i in range(len(s)):
        ch=s[i]
        left_substr=s[0:i]
        right_substr=s[i+1:]
        rest=left_substr+right_substr
        permute(rest,k+ch)
k=""
s=input()
permute(s,k)