import time
start_time = time.time()
fi = open('kargerMinCut.txt')
#fi = open('test_case.txt')
graph=[]
for line in fi:
    string = line.strip()
    vertex = int(string[:string.find('\t')])
    string = string[string.find('\t')+1:]
    connected_to=[]
    while string.find('\t')!=-1:
        connected_to.append(int(string[:string.find('\t')]))
        string = string[string.find('\t')+1:]
    connected_to.append(int(string))    
    graph.append([vertex, connected_to])
#created a list with each row as an item in the list
#the rows themselves are lists with the 1st element as the vertex
#the 2nd element of the row is a list containing all the adjacent vertices
fi.close()



temp_graph=graph
import random
while len(temp_graph) > 2:
    rn = random.randint(0,len(temp_graph)-1)
    selected_vertex_1 = temp_graph[rn][0]
    selected_vertex_2 = temp_graph[rn][1][random.randint(0,len(temp_graph[rn][1])-1)]
    for vc in temp_graph:
        if vc[0]==selected_vertex_2:
            vc[0]=selected_vertex_1
        vc[1]=[selected_vertex_1 if x==selected_vertex_2 else x for x in vc[1]]
    new_conn=[]
    #Replacing all occurences of selected_vertex_2 with selected_vertex_1
    
    #print selected_vertex_1, selected_vertex_2, temp_graph
    #print 'hi'
    for vc in temp_graph:
        if vc[0]==selected_vertex_1:
            for v in vc[1]:
                if v!=selected_vertex_1:
                    new_conn.append(v)
    temp_graph = [vc for vc in temp_graph if vc[0]!=selected_vertex_1 ]
    temp_graph.append([selected_vertex_1, new_conn])
    #Removed both rows of selcted_vertex_1 AND inserted row with fused vertices
    #print temp_graph
     
print len(temp_graph[0][1])
print "Time taken for the Randomized Contraction Algorithm to run"
print time.time() - start_time, "seconds"
