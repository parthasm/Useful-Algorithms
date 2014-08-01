InputFileName = input("Enter input file name with extension within quotes : ")
import time
start_time = time.time()
fi = open(InputFileName)
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

import sys
import os
os.chdir("../Single_Source_Shortest_Path")
sys.path.append(os.getcwd())
import SSSP
SSSP.setGraph(Graph)

minimums=[]

for vertex in Graph:
    li = SSSP.BellmanFord(vertex,True,NumVertices)
    if li:
        minimums.append(min(li))
    else:
        break

if minimums:
    print min(minimums)    
print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
