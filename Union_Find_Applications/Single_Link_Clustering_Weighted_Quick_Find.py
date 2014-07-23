
import time
start_time = time.time()

fi = open('clustering1.txt')
EdgeList=[]

Roots=[]
Roots.append([0,0])#index of list => vertex; element of list => root,size of cluster
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
Roots*=(NumVertices+1)
for i in range(NumVertices+1):
    Roots[i]=[i,1]

EdgeList = sorted(EdgeList, key=lambda x:x[2])
#for e in EdgeList:
 #   print e
    
NumClusters=NumVertices
for k,e in enumerate(EdgeList):
    if Roots[e[0]][0]!=Roots[e[1]][0]:
        size0 = Roots[e[0]][1]
        size1 = Roots[e[1]][1]
        totalSize = size0+size1
        if size0>size1:
            temp = Roots[e[1]][0]
            for i,v in enumerate(Roots):
                if v[0]==temp:
                    Roots[i][0]=Roots[e[0]][0]
                    Roots[i][1]=totalSize
                if v[0]==Roots[e[0]][0]:
                    Roots[i][1]=totalSize
        else:
            temp = Roots[e[0]][0]
            for i,v in enumerate(Roots):
                if v[0]==temp:
                    Roots[i][0]=Roots[e[1]][0]
                    Roots[i][1]=totalSize
                if v[0]==Roots[e[1]][0]:
                    Roots[i][1]=totalSize            
        NumClusters-=1
        #print Roots
        if NumClusters==4:
            break

for i in range(k+1,len(EdgeList)):            
    if Roots[EdgeList[i][0]][0]!=Roots[EdgeList[i][1]][0]:
        print EdgeList[i][2]
        break

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
