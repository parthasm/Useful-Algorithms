def bfs(v,w):
    q = deque([])
    q.append(v)
    bfsSet = set()
    while len(q)!=0:
        st = q.popleft()
        bfsSet.add(st)
        connectedVertices = Graph[st]
        for vert in connectedVertices:
            if vert==w:
                return True
            if not ((vert in bfsSet) or (vert in q)):
                q.append(vert)
    return False

from collections import deque
import time
start_time = time.time()

fi = open('edges.txt')
EdgeList=[]
Graph={}

for index,line in enumerate(fi):
    if index!=0:
        details = line.split()
        v = int(details[0])
        w = int(details[1])
        EdgeList.append((v,w,int(details[2])))
        
fi.close()

EdgeList = sorted(EdgeList, key=lambda x:x[2])
MinSumEdges=0
for e in EdgeList:
    Graph[e[0]]=Graph.get(e[0],[])
    Graph[e[1]]=Graph.get(e[1],[])
    if not bfs(e[0],e[1]):
        Graph[e[0]].append(e[1])
        Graph[e[1]].append(e[0])
        MinSumEdges+=e[2]

print MinSumEdges

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
