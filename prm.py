def prim(G,s):
    q,p,visit={},{},[i for i in G]
    for i in G:
        q[i]=float('inf')
    q[s],p[s]=0,None
    while q:
        u=min(q.items(), key=lambda x: x[1])[0]
        if u in q: del q[u]
        print(u)
        for v in G[u]:
            if v in q and G[v][u]<q[v]:
                p[v]=u
                q[v]=G[u][v]
    return p
g={0: {1: 3, 3: 6, 2: 1}, 1: {0: 3, 4: 3, 2: 5}, 4: {1: 3, 5: 6, 2: 6}, 5: {4: 6, 3: 2, 2: 4}, 3: {5: 2, 0: 6, 2: 5}, 2: {0: 1, 1: 5, 4: 6, 5: 4, 3: 5}}
print(prim(g,0))
