from __future__ import division

import time
start_time = time.time()

fi = open('edges.txt')

Graph={}
UnProcessedVertices = set()
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
        UnProcessedVertices.add(v)
        UnProcessedVertices.add(w)

fi.close()
#--
#print len(UnProcessedVertices), len(Graph)
#--
import sys
import os
os.chdir("..")
sys.path.append(os.getcwd())
#Initializing the heap, with source vertex as 1
import Heap
di = Graph[1]
for v in Graph.keys():
    if v!=1:
        Heap.insert([v,di.get(v,99999999)])

UnProcessedVertices.remove(1)

#--
#print Heap.lengthHeap()
#Heap.printHeap()
#print di
#--
while len(UnProcessedVertices) > 0:
    #---
    #Heap.printHeap()
    #---
    li = Heap.popMin()
    UnProcessedVertices.remove(li[0])
    MinSumEdges+=li[1]
    di = Graph[li[0]]
    for w in di:
        if w in UnProcessedVertices:
            Heap.modifyKeyIfBetter(w,di[w])
            #Ensuring that for every vertex not yet processed,
            #its key is the least cost edge across the cut

print MinSumEdges
            
print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
