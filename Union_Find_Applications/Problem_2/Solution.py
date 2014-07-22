import time
start_time = time.time()

NumVertices = 0
NumBits = 0

#fi = open('test_case.txt')
fi = open('clustering_big.txt')
Vertices=[]#Every vertex or node is stored here as a list of numeric zeros or ones
for index,line in enumerate(fi):
    li = line.split()
    if index==0:
        NumVertices = int(li[0])
        NumBits = int(li[1])
    
    #elif index>2300 and index<3201:
    else:        
        li = [ bool(int(w)) for w in li]
        Vertices.append(li)        

fi.close()
#NumVertices = 900

ClusterIndices = [0]
ClusterIndices*=NumVertices
for i in range(NumVertices):
    ClusterIndices[i]=[i,1]

SetClusterIndicesCovered = set()

for i,v in enumerate(Vertices):
    #if ClusterIndices[i] not in SetClusterIndicesCovered:
    if True:
        liCombos = []
        liCombos.append(v)
        for outer in range(NumBits):
            w=v[:]
            w[outer]=not v[outer]
            liCombos.append(w)
            for inner in range(outer+1,NumBits):
                x=w[:]
                x[inner]=not w[inner]
                liCombos.append(x)
        #if i==0:
         #   for n in liCombos:
          #      print n,'\n\n'
        for node in liCombos:
            for j in range(i+1,NumVertices):
                flag=True
                for bitPosition in range(NumBits):
                    if node[bitPosition]!=Vertices[j][bitPosition]:
                        flag=False
                        break
                if flag:
                    totalSize = ClusterIndices[j][1]+ClusterIndices[i][1]
                    if ClusterIndices[j][1]<ClusterIndices[i][1]:
                        temp=ClusterIndices[j][0]
                        for index in range(NumVertices):
                            if temp==ClusterIndices[index][0]:
                                ClusterIndices[index][0]=ClusterIndices[i][0]
                                ClusterIndices[index][1]=totalSize
                            elif ClusterIndices[index][0]==ClusterIndices[i][0]:
                                ClusterIndices[index][1]=totalSize
                    else:
                        temp=ClusterIndices[i][0]
                        for index in range(NumVertices):
                            if temp==ClusterIndices[index][0]:
                                ClusterIndices[index][0]=ClusterIndices[j][0]
                                ClusterIndices[index][1]=totalSize
                            elif ClusterIndices[index][0]==ClusterIndices[j][0]:
                                ClusterIndices[index][1]=totalSize
    #print ClusterIndices                    
    
ClusterIndices = [w[0] for w in ClusterIndices] 

print len(set(ClusterIndices))
print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
