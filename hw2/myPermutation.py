def perm(l):
    p=[]
    return permNext(l,p)

def permNext(l,p):
    i=len(p)
    if(i==len(l)):
        print(p)
        return
    for _ in l:
        if not _ in p:
            p.append(_)
            permNext(l,p)
            p.pop()

l=['x','y','z']
perm(l)