#fi = open('kargerMinCut.txt')
fi = open('test_case_bfs.txt')
graph=[]
for line in fi:
    string = line.strip()
    vertex = string[:string.find('\t')]
    string = string[string.find('\t')+1:]
    connected_to=[]
    while string.find('\t')!=-1:
        connected_to.append(string[:string.find('\t')])
        string = string[string.find('\t')+1:]
    connected_to.append(string)    
    graph.append([vertex, connected_to])
#created a list with each row as an item in the list
#the rows themselves are lists with the 1st element as the vertex
#the 2nd element of the row is a list containing all the adjacent vertices
fi.close()


from collections import deque
q = deque([])
q.append(graph[0][0])
bfs = []
while len(q)!=0:
    st = q.popleft()
    bfs.append(st)
    vc = [vc for vc in graph if vc[0]==st]
    vc = vc[0]
    for v in vc[1]:
        if not ((v in bfs) or (v in q)):
            q.append(v)
            
print bfs
