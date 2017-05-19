import time
from heapq import heappush, heappop
def Dijkstra(graph, start):
    A={}
    queue = [( 0,start)]
    while queue:
        path_len, v = heappop(queue)
        if v not in A : # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if w not in A :
                    heappush(queue, (path_len + edge_len, w))

    return A
graph = {0 : {1:6, 2:8},
1 : {4:11},
2 : {3: 9},
3 : {},
4 : {5:3},
5 : {2: 7, 3:4}}
start=time.clock()
print(Dijkstra(graph,0))
print('%f' %(time.clock()-start))
