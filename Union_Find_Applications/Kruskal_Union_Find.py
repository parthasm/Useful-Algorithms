i = int(input('Enter 1 for Quick Find,'
          '2 for Quick Union and 3 for Weighted Quick Find: '))
if i==1:
    from Quick_Find import initialize
    from Quick_Find import connected
    from Quick_Find import union
elif i==2:
    from Quick_Union import initialize
    from Quick_Union import connected
    from Quick_Union import union
elif i==3:    
    from Weighted_Quick_Find import initialize
    from Weighted_Quick_Find import connected
    from Weighted_Quick_Find import union

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
initialize(NumVertices)

EdgeList = sorted(EdgeList, key=lambda x:x[2])

   
MinSumEdges=0
for k,e in enumerate(EdgeList):
    if not connected(e[0],e[1]):
        union(e[0],e[1])
        MinSumEdges+=e[2]                        
            
print MinSumEdges

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
