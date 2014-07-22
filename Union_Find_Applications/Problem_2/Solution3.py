import time
start_time = time.time()

NumVertices = 0
NumBits = 0

#fi = open('test_case.txt')
fi = open('clustering_big.txt')
Vertices=[]#Every vertex or node is stored here as a list of numeric zeros or ones
VerticesDict = {}
for index,line in enumerate(fi):
    li = line.split()
    if index==0:
        NumVertices = int(li[0])
        NumBits = int(li[1])
    
    elif index<10001:
    #else:        
        s = ''.join(li)
        i = int(s,2)
        Vertices.append(i)
        VerticesDict[i]=VerticesDict.get(i,set())
        VerticesDict[i].add(index-1)
       
fi.close()
NumVertices = 10000
the300 = []

for outer in range(NumBits):
    li=[]
    for bitPosition in range(NumBits):
        if outer!=bitPosition:
            li.append('0')
        else:
            li.append('1')
    s = ''.join(li)
    i = int(s,2)
    the300.append(i)

for outer in range(NumBits):
    for inner in range(outer+1,NumBits):
        li=[]
        for bitPosition in range(NumBits):
            if outer!=bitPosition and inner!=bitPosition:
                li.append('0')
            else:
                li.append('1')
        s = ''.join(li)
        i = int(s,2)
        the300.append(i)

the300.append(0)
#for s in the300:
 #   print bin(s)
            
ClusterIndices = {}
ReverseClusterIndices={}
for i in range(NumVertices):
    se = VerticesDict[Vertices[i]]
    for index in se:
        if ClusterIndices.get(index,-1)!=-1:
            break
        ClusterIndices[index]=i
        ReverseClusterIndices[i] = ReverseClusterIndices.get(i,[])
        ReverseClusterIndices[i].append(index)
#print len(set(ClusterIndices.keys()))    
#print len(set(ClusterIndices.values()))
#for i in ClusterIndices:
    #print i


for index,v in enumerate(Vertices):
    for t in the300:
        w=v^t
        se = VerticesDict.get(w,set())
        if se:
            elem = se.pop()
            #se.add(elem)
            if ClusterIndices[index]!=ClusterIndices[elem]:
                temp = ClusterIndices[elem]
                #for i,c in ClusterIndices.items():
                 #   if c==temp:
                  #      ClusterIndices[i]=ClusterIndices[index]
                indices = ReverseClusterIndices[temp]                  
                for i in indices:
                    ClusterIndices[i]=ClusterIndices[index]
                ReverseClusterIndices[ClusterIndices[index]].extend(indices)
                del ReverseClusterIndices[temp]
    
print len(set(ClusterIndices.values()))

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
