for _ in range(int(input())):
    n=int(input())
    l1=[]
    l=list(map(int,input().split()))
    l.sort()
    for i in range(n-1):
        a=(l[i])^(l[i+1])
        l1.append(a)
    print(min(l1))