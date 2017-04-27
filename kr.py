def krushal(g,vertex):
    t,a=[],{}
    for i in vertex:
        a[i]=set({i})
    for edge in sorted(g):
        for v1,v2 in g[edge]:
            if v1 not in a[v2]:
                t.append((v1,v2))
                a[v1]=a[v1].union(a[v2])
                for i in a[v1]:
                    a[i]=a[v1]
    return t
g={3:[{0,1},{1,4}],6:[{4,5},{0,3},{2,4}],2:[{3,5}],1:[{0,2}],5:[{1,2},{3,0}],4:[{2,5}]}#g={weight:{vertex1,vertex2}}
vertex=[0,1,2,3,4,5]
for edge in g:
    for v1,v2 in g[edge]:
        print("from ",v1,"---->",v2," distance ",edge)
a=krushal(g,vertex)
for i in a:
    print(i[0],"----------->",i[1])
