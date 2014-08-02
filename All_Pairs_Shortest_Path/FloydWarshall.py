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
       

        Graph[v] = Graph.get(v,{})
        Graph[v][w] = e
    else:
       NumVertices = int(line.split()[0]) 
        

#print Graph    
#created a dictionary with each source vertex as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the destination vertex and the value is the edge cost  
fi.close()

A = [[ 1000000 for i in range(NumVertices)] for j in range(NumVertices)]
B = [[ 1000000 for i in range(NumVertices)] for j in range(NumVertices)]
NegCycle = False

for i in range(NumVertices):
    for j in range(NumVertices):
        if i==j:
            A[i][j]=0
        elif Graph.get(i+1,-1)!=-1:
            if Graph[i+1].get(j+1,1000000)!=1000000:
                A[i][j]=Graph[i+1][j+1]
    
for k in range(NumVertices):
    for i in range(NumVertices):
        for j in range(NumVertices):
            B[i][j]=min(A[i][j],A[i][k]+A[k][j])
    for i in range(NumVertices):
        if B[i][i]<0:
            NegCycle = True
            break
    if NegCycle:
        break
    A = [li[:] for li in B]
    


if NegCycle:
    print "Graph has negative cycle"
else:    
    print "Shortest shortest path distance = " , min([min(li) for li in A])
    
print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
