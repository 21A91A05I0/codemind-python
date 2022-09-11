def isvowel(c):
    return(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O'or c=='U')
def reversevowel(str):
    i=0
    j=len(str)-1
    while(i<j):
        if not isvowel(str[i]):
            i+=1
            continue
        if(not isvowel(str[j])):
            j-=1
            continue
        str[i],str[j]=str[j],str[i]
        i+=1
        j-=1
    return str
if __name__=="__main__":
    str=input()
    print(*reversevowel(list(str)),sep="")