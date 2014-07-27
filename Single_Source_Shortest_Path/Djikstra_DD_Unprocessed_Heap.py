
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
        Graph[v] = Graph.get(v,{})
        Graph[v][w] = Graph[v].get(w,[0,0])
        Graph[v][w][0]=e

        Graph[w] = Graph.get(w,{})
        Graph[w][v] = Graph[w].get(v,[0,0])
        Graph[w][v][1]=e
#print Graph    
#created a dictionary with each vertex v as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the connected vertex w and the value is a 2-element list.
#The 1st element of the list is assigned the edge cost
#if it is a forward edge (from v to w)and
#the 2nd element is assigned the edge cost
#if it is a backward edge (from w to v)

fi.close()

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
        if di[v][1]!=0 and dict_shortest_path.get(v,-1)==-1:
            Heap.modifyKeyIfBetter(v,w_score[1]+di[v][1])



print dict_shortest_path[7]

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"

