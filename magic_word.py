T=int(input())
a=[67,71,73,79,83,89,97,101,103,107,109,113,127]
def less(l):
    i=11
    while l<a[i] and i>=0:
        i=i-1
    return a[i]
def greater(g):
    i=11
    while g<a[i] and i>=0:
       i=i-1
    if i==11:
        return a[i]
    else:    
        return a[i+1]
for i in range(0,T):
    S=int(input())
    st=input()
    word=""
    for c in st:
        l=less(ord(c))
        g=greater(ord(c))
        if abs(ord(c)-l)>abs(g-ord(c)):
            word=word+chr(g)
        else:
            word=word+chr(l)
    print(word)