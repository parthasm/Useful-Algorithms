import time
start_time = time.time()
fi = open('kargerMinCut.txt')
#fi = open('test_case.txt')
Graph={}
for line in fi:
    li = line.split()  
    Graph[li[0]] = li[1:]
#created a list with each row as an item in the list
#the rows themselves are lists with the 1st element as the vertex
#the 2nd element of the row is a list containing all the adjacent vertices
fi.close()



TempGraph=Graph
import random
while len(TempGraph) > 2:
    rn = random.randint(0,len(TempGraph)-1)
    selected_vertex_1 = TempGraph.keys()[rn]
    selected_vertex_2 = TempGraph[selected_vertex_1][random.randint(0,len(TempGraph[selected_vertex_1])-1)]
    li = TempGraph[selected_vertex_2]
    del TempGraph[selected_vertex_2]
    TempGraph[selected_vertex_1].extend(li)
    for vertex in TempGraph:
        TempGraph[vertex]=[selected_vertex_1 if x==selected_vertex_2 else x for x in TempGraph[vertex]]
    new_conn=[]
    #Replacing all occurences of selected_vertex_2 with selected_vertex_1
    
    #print selected_vertex_1, selected_vertex_2, TempGraph
    #print 'hi'
    
    TempGraph[selected_vertex_1]=[v for v in TempGraph[selected_vertex_1] if v!=selected_vertex_1]
    #Removed both rows of selcted_vertex_1 AND inserted row with fused vertices
    #print TempGraph
     
print len(TempGraph[selected_vertex_1])
print "Time taken for the Randomized Contraction Algorithm to run"
print time.time() - start_time, "seconds"
