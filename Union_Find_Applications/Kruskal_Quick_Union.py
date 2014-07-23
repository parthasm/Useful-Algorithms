import Quick_Union  

import time
start_time = time.time()

fi = open('edges.txt')
EdgeList=[]


NumVertices=0

for index,line in enumerate(fi):
    if index!=0:
        details = line.split()
        v = int(details[0])
        w = int(details[1])
        EdgeList.append((v,w,int(details[2])))
    else:
        NumVertices=int(line.split()[0])
fi.close()

##Initializing the roots

Quick_Union.initialize(NumVertices)

EdgeList = sorted(EdgeList, key=lambda x:x[2])

  
MinSumEdges=0
for k,e in enumerate(EdgeList):
    if not Quick_Union.connected(e[0],e[1]):
        Quick_Union.union(e[0],e[1])
        MinSumEdges+=e[2]                        
            
print MinSumEdges

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
