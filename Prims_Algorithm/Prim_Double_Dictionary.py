from __future__ import division

import time
start_time = time.time()

fi = open('edges.txt')

Graph={}
ProcessedVertices = set()
MinSumEdges=0

for index,line in enumerate(fi):
    if index!=0:
        edge = line.split()
        #CatWordDict[cat]=CatWordDict.get(cat,{})
        v = int(edge[0])
        w = int(edge[1])
        e = int(edge[2])
        Graph[v]= Graph.get(v,{})
        Graph[w]= Graph.get(w,{})
        Graph[v][w] = e
        Graph[w][v] = e
        
        
fi.close()        
numVertices = len(Graph)
#numEdges = 0    
#for vertex in Graph:
 #  numEdges+=len(Graph[vertex]) 

#print numVertices, (numEdges/2)
 
ProcessedVertices.add(1)
v=1
while len(ProcessedVertices)<numVertices:
    minEdge = 9999999999
    VertexToBeAdded=0
    for v in ProcessedVertices:
        for w  in Graph[v]:
            if w not in ProcessedVertices and Graph[v][w]<minEdge:
                minEdge=Graph[v][w]
                VertexToBeAdded=w

    MinSumEdges+= minEdge
    ProcessedVertices.add(VertexToBeAdded)

print     MinSumEdges
                
    
print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
