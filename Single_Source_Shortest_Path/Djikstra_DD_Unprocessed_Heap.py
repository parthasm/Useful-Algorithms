
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
        Graph[v][w]=e
#print Graph    
#created a dictionary with each source vertex v as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the destination vertex w and the value is the edge cost

fi.close()
import SSSP
SSSP.setGraph(Graph)
ShortestPaths = SSSP.DjikstraHeap(1,len(Graph))
print ShortestPaths[7]

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
