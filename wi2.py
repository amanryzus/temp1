import bisect
def weighted_interval_scheduling(G):
    S,Z={},[]
    G.sort(key=lambda x:x[1])
    start = [x[0] for x in G]
    end = [x[1]-1 for x in G]
    S[0] = 0
    S[1] = G[0][2]
    for i in range(2,len(G)+1):
        S[i] = max(S[i-1],G[i-1][2]+S[bisect.bisect_left(end, start[i-1])])
    return S[len(G)]
G = [(43,70,27),(3,18,24),(65,99,45),(20,39,26),(45,74,26),(10,28,20),(78,97,23),(0,9,22)]#g={(start,finsh,value)}
print(G)
#G=[(1, 2, 50),(3, 5, 20),(6, 19, 100),(2, 100, 200)]
#print(G)
print(weighted_interval_scheduling(G))
