import time
start_time = time.time()
fi = open('kargerMinCut.txt')
#fi = open('test_case.txt')
Graph=[]
for line in fi:
    li = line.split()  
    Graph.append([li[0], li[1:]])
#created a list with each row as an item in the list
#the rows themselves are lists with the 1st element as the vertex
#the 2nd element of the row is a list containing all the adjacent vertices
fi.close()



TempGraph=Graph
import random
while len(TempGraph) > 2:
    rn = random.randint(0,len(TempGraph)-1)
    selected_vertex_1 = TempGraph[rn][0]
    selected_vertex_2 = TempGraph[rn][1][random.randint(0,len(TempGraph[rn][1])-1)]
    for vc in TempGraph:
        if vc[0]==selected_vertex_2:
            vc[0]=selected_vertex_1
        vc[1]=[selected_vertex_1 if x==selected_vertex_2 else x for x in vc[1]]
    new_conn=[]
    #Replacing all occurences of selected_vertex_2 with selected_vertex_1
    
    #print selected_vertex_1, selected_vertex_2, TempGraph
    #print 'hi'
    for vc in TempGraph:
        if vc[0]==selected_vertex_1:
            for v in vc[1]:
                if v!=selected_vertex_1:
                    new_conn.append(v)
    TempGraph = [vc for vc in TempGraph if vc[0]!=selected_vertex_1 ]
    TempGraph.append([selected_vertex_1, new_conn])
    #Removed both rows of selcted_vertex_1 AND inserted row with fused vertices
    #print TempGraph
     
print len(TempGraph[0][1])
print "Time taken for the Randomized Contraction Algorithm to run"
print time.time() - start_time, "seconds"
