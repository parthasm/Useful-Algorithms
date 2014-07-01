import time
start_time = time.time()
fi = open('kargerMinCut.txt')
#fi = open('test_case.txt')
graph={}
for line in fi:
    string = line.strip()
    vertex = int(string[:string.find('\t')])
    string = string[string.find('\t')+1:]
    connected_to=[]
    while string.find('\t')!=-1:
        connected_to.append(int(string[:string.find('\t')]))
        string = string[string.find('\t')+1:]
    connected_to.append(int(string))    
    graph[vertex] = connected_to
#created a list with each row as an item in the list
#the rows themselves are lists with the 1st element as the vertex
#the 2nd element of the row is a list containing all the adjacent vertices
fi.close()



temp_graph=graph
import random
while len(temp_graph) > 2:
    rn = random.randint(0,len(temp_graph)-1)
    selected_vertex_1 = temp_graph.keys()[rn]
    selected_vertex_2 = temp_graph[selected_vertex_1][random.randint(0,len(temp_graph[selected_vertex_1])-1)]
    li = temp_graph[selected_vertex_2]
    del temp_graph[selected_vertex_2]
    temp_graph[selected_vertex_1].extend(li)
    for vertex in temp_graph:
        temp_graph[vertex]=[selected_vertex_1 if x==selected_vertex_2 else x for x in temp_graph[vertex]]
    new_conn=[]
    #Replacing all occurences of selected_vertex_2 with selected_vertex_1
    
    #print selected_vertex_1, selected_vertex_2, temp_graph
    #print 'hi'
    
    temp_graph[selected_vertex_1]=[v for v in temp_graph[selected_vertex_1] if v!=selected_vertex_1]
    #Removed both rows of selcted_vertex_1 AND inserted row with fused vertices
    #print temp_graph
     
print len(temp_graph[selected_vertex_1])
print "Time taken for the Randomized Contraction Algorithm to run"
print time.time() - start_time, "seconds"
