
import time
start_time = time.time()
fi = open('dijkstraData.txt')
#fi = open('test_case.txt')
Graph={}
UnProcessedVertices = set()
for line in fi:
    li = line.split()
    vertex = li[0]
    for we in li[1:]:
        we = we.split(',')
        Graph[vertex] = Graph.get(vertex,{})
        Graph[we[0]] = Graph.get(we[0],{})
        Graph[vertex][we[0]] = int(we[1])
        Graph[we[0]][vertex] = int(we[1])
        UnProcessedVertices.add(vertex)
        UnProcessedVertices.add(we[0])
#print Graph    
#created a dictionary with each vertex as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the connected vertex and the value is the edge cost        
fi.close()

numVertices = len(Graph)

dict_shortest_path={}
dict_shortest_path['1']=0
UnProcessedVertices.remove('1')

while len(UnProcessedVertices) > 0:
    minimum = 1000000
    for w in UnProcessedVertices:
        di = Graph[w]
        for v in di:
            if dict_shortest_path.get(v,-1)!=-1:
                sp = dict_shortest_path[v]+Graph[v][w]
                if sp < minimum:
                    minimum = sp
                    w_star = w
    dict_shortest_path[w_star]=minimum                   
    UnProcessedVertices.remove(w_star)

print dict_shortest_path['7']

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"

