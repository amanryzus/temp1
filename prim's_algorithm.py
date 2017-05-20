def prim(g,s):
    q={}
    p={}
    visit=[i for i in g]
    for i in g:
        q[i]=float('inf')
    while q:
        u=min(q.items(),key=lambda x: x[1] )[0]
        if u in q:del q[u]
        for v in g[u]:
            if v in q and g[u][v]<q[v]:
                p[v]=u
                q[v]=g[u][v]
    return p
g={1:{2:4,4:8},2:{3:3,4:1},3:{5:8,4:7},4:{5:3},5:{}}
path,a=prim(g,1),0
for v1,v2 in path.items():
    print(v2,"->",v1,"dist",g[v2][v1] if v2!=None else 0)
    if v2!=None:
        a=a+g[v2][v1]
print(a)

