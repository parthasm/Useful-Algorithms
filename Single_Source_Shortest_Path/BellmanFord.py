
import time
start_time = time.time()
fi = open('Input.txt')
#fi = open('test_case.txt')
Graph={}
n=0
for line in fi:
    li = line.split()
    v = int(li[0])
    for we in li[1:]:
        we = we.split(',')
        w = int(we[0])
        e = int(we[1])
        Graph[v] = Graph.get(v,{})
        Graph[v][w] = e

    n+=1
#print Graph    
#created a dictionary with each vertex as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the connected vertex and the value is the edge cost  
fi.close()

NumVertices = len(Graph)
A=[1000000]
B=[1000000]
A*=(NumVertices+1)
B*=(NumVertices+1)

#Assuming 1 is the source vertex
A[1]=0
B[1]=0

for i in range(1,NumVertices+1):
    for v in Graph:
        minimum = A[v]
        ws = Graph[v]
        for w in ws:
            if minimum > Graph[v][w]+A[w]:
                minimum = Graph[v][w]+A[w]
        B[v]=minimum
    A=B[:]        


print A[7]
print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
