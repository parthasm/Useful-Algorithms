
import time
start_time = time.time()
fi = open('tc2.txt')
#fi = open('test_case.txt')
Graph={}
NumVertices = 0
for index,line in enumerate(fi):
    if index!=0:
        li = line.split()
        v = int(li[0])
        w = int(li[1])
        e = int(li[2])
       

        Graph[w] = Graph.get(w,{})
        Graph[w][v] = e
    else:
       NumVertices = int(line.split()[0]) 
        


#print Graph    
#created a dictionary with each destination vertex as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the source vertex and the value is the edge cost  
fi.close()


minimums=[]

for vertex in Graph:
    
    A=[1000000]
    B=[1000000]
    A*=(NumVertices+1)
    B*=(NumVertices+1)

    #'vertex' is the source vertex
    A[vertex]=0
    B[vertex]=0
    
    OptimaReached=True
    for i in range(1,NumVertices+2):
        OptimaReached=True
        for v in Graph:
            minimum = A[v]
            di = Graph[v]
            for w in di:
    
                if minimum > di[w]+A[w]:
                    minimum = di[w]+A[w]
                    
            B[v]=minimum
            if A[v]!=B[v]:
                OptimaReached=False
        if OptimaReached:
            break        
        A=B[:]        
    if not OptimaReached:
        print 'Graph has negative cycle'
        break
    minimums.append(min(A))
print min(minimums)    
print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
