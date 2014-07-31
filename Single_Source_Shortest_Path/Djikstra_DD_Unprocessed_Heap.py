
import time
start_time = time.time()
fi = open('Input.txt')
#fi = open('test_case.txt')
Graph={}
for line in fi:
    li = line.split()
    v = int(li[0])
    for we in li[1:]:
        we = we.split(',')
        w = int(we[0])
        e = int(we[1])
        Graph[w] = Graph.get(w,{})
        Graph[w][v]=e
#print Graph    
#created a dictionary with each destination vertex v as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the source vertex w and the value is the edge cost

fi.close()

import sys
import os
os.chdir("..")
sys.path.append(os.getcwd())
import Heap
for v in Graph:
    if v!=1:
        Heap.insert([v,1000000])
    else:
        Heap.insert([v,0])

numVertices = len(Graph)

dict_shortest_path={}

while Heap.lengthHeap() > 0 :
    w_score = Heap.popMin()
    w = w_score[0]
    dict_shortest_path[w]=w_score[1]
    di = Graph[w]
    for v in di:
        if dict_shortest_path.get(v,-1)==-1:
            Heap.modifyKeyIfBetter(v,w_score[1]+di[v])



print dict_shortest_path[7]

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"

