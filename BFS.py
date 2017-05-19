import time
a=int(input("number of nodes"))
g={}    #create an empty dic
for i in range(a):
    print("for",i+1,"enter all the conecting nodes:")
    b=list(map(int,input().split()))

#here creates the graph G
    for j in b:
        if i+1 not in g:
            g.update({i+1:[j]}) #creates a dic with key and val as nodes and connecting nodes
        else:
            g[i+1].append(j)    #here g[i] contains the list of connecting nodes

#print(g)

def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend([i for i in graph[vertex] if i not in visited])
    return visited
s=int(input("starting point of graph"))
start_time=time.clock()
print(bfs(g,s))
print(time.clock()-start_time)
