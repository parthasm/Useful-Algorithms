Roots=[]
Roots.append(0)#index of list => vertex; element of list => root,size of cluster
Sizes=[]
Sizes.append(0)
ReverseRoots={}

def initialize(n):
    global Roots
    global Sizes
    Roots*=(n+1)
    Sizes*=(n+1)
    for i in range(n+1):
        Roots[i]=i
        Sizes[i]=1
        ReverseRoots[i]=[]
        ReverseRoots[i].append(i)
        
def findRoot(v):
    return Roots[v]      

def union(v,w):
    sizev = Sizes[Roots[v]]
    sizew = Sizes[Roots[w]]
    totalSize=sizev+sizew
    Sizes[Roots[v]]=totalSize
    Sizes[Roots[w]]=totalSize
    if sizev>sizew:
        temp = Roots[w]
        li=ReverseRoots[temp]
        for index in li:
            Roots[index]=Roots[v]
        del ReverseRoots[temp]
        ReverseRoots[Roots[v]].extend(li)
               
    else:
        temp = Roots[v]
        li=ReverseRoots[temp]
        for index in li:
            Roots[index]=Roots[w]
        del ReverseRoots[temp]
        ReverseRoots[Roots[w]].extend(li)      

                
def connected(v,w):
    return findRoot(v)==findRoot(w)
