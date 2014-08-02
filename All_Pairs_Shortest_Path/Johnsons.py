InputFileName = input("Enter input file name with extension within quotes : ")
import time
start_time = time.time()
fi = open(InputFileName)
GraphBF={}
GraphDJ={}
NumVertices = 0
for index,line in enumerate(fi):
    if index!=0:
        li = line.split()
        v = int(li[0])
        w = int(li[1])
        e = int(li[2])
       
        
        GraphDJ[v] = GraphDJ.get(v,{})
        GraphDJ[v][w] = e
        
        GraphBF[w] = GraphBF.get(w,{})
        GraphBF[w][v] = e
    else:
       NumVertices = int(line.split()[0]) 
        


#for GraphBF   
#created a dictionary with each destination vertex as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the source vertex and the value is the edge cost

#for GraphDJ
#created a dictionary with each source vertex as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the destination vertex and the value is the edge cost  
fi.close()

#Adding the fake source vertex
for i in range(NumVertices):
    GraphBF[i+1]=GraphBF.get(i+1,{})
    GraphBF[i+1][0]=0

import sys
import os
os.chdir("../Single_Source_Shortest_Path")
sys.path.append(os.getcwd())
import SSSP
SSSP.setGraph(GraphBF)

li=SSSP.BellmanFord(0,True,NumVertices+1)
if li:        
    for v in GraphDJ:
        di=GraphDJ[v]
        for w in di:
            GraphDJ[v][w]=di[w]+li[v]-li[w]
    SSSP.setGraph(GraphDJ)
    ShortestDistances=[]
    for i in range(NumVertices):
        di = SSSP.DjikstraHeap(i+1,NumVertices )
        ks = di.keys()
        for k in ks:
            ShortestDistances.append(di[k]+li[k]-li[i+1])

    print "Shortest shortest distance = " , min(ShortestDistances)        
print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
