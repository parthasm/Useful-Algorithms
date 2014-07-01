def dfs(graph,seen,v):
    seen.append(v)
    vc = [vc for vc in graph if vc[0]==v]
    print vc[0]
    vc = vc[0]
    for v1 in vc[1]:
        if v1 not in seen:
            dfs(graph,seen,v1)
    

#fi = open('kargerMinCut.txt')
fi = open('test_case_dfs_3.txt')
graph=[]
for line in fi:
    string = line.strip()
    tab_index = string.find('\t')
    vertex = string[:tab_index]
    string = string[tab_index+1:]
    connected_to=[]
    while tab_index!=-1:
        connected_to.append(string[:tab_index])
        string = string[tab_index+1:]
        tab_index = string.find('\t')
    connected_to.append(string)    
    graph.append([vertex, connected_to])
#print graph    
#created a list with each row as an item in the list
#the rows themselves are lists with the 1st element as the vertex
#the 2nd element of the row is a list containing all the adjacent vertices

import sys
sys.setrecursionlimit(10000)
seen=[]
dfs(graph,seen,graph[0][0])
print seen
