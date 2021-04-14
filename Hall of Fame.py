def f(l,n,m):
    res,i,c=[],0,0
    while i<len(l):
        res.append(l[i:i+m])
        i+=1
    l1=res
    for j in range(len(l1)):
        if sum(l1[j])==n:
            c+=1
    return c
l=list(map(int,input().split()))
n,m=map(int,input().split())
print(f(l,n,m)git remote -v