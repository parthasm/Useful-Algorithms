
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
        Graph[v][w] = e

#print Graph    
#created a dictionary with each source vertex v as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the destination vertex w and the value is the edge cost
fi.close()

NumVertices = len(Graph)

dict_shortest_path={}
dict_shortest_path[1]=0
while True:
    minimum = 1000000
    for v in dict_shortest_path.keys():
        dests= Graph[v]
        for d in dests:            
            if dict_shortest_path.get(d,-1)==-1:
                sp = dict_shortest_path[v]+dests[d]
                if sp < minimum:
                    minimum = sp
                    w_star = d
    dict_shortest_path[w_star]=minimum       
    if len(dict_shortest_path)==NumVertices:
        break

print dict_shortest_path[7]

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"

