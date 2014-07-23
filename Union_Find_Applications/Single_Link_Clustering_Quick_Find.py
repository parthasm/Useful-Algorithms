import Quick_Find
import time
start_time = time.time()

fi = open('clustering1.txt')
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
Quick_Find.initialize(NumVertices)

EdgeList = sorted(EdgeList, key=lambda x:x[2])
#for e in EdgeList:
 #   print e
    
NumClusters=NumVertices
for k,e in enumerate(EdgeList):
    if not Quick_Find.connected(e[0],e[1]):
        Quick_Find.union(e[0],e[1])
                
        NumClusters-=1
        #print Roots
        if NumClusters==4:
            break

for i in range(k+1,len(EdgeList)):            
    if not Quick_Find.connected(EdgeList[i][0],EdgeList[i][1]):        
        print EdgeList[i][2]
        break

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
