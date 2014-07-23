Roots=[]
Roots.append([0,0])#index of list => vertex; element of list => root,size of cluster

def initialize(n):
    global Roots
    Roots*=(n+1)
    for i in range(n+1):
        Roots[i]=[i,1]

def findRoot(v):
    return Roots[v][0]       

def union(v,w):
    sizev = Roots[v][1]
    sizew = Roots[w][1]
    totalSize=sizev+sizew
    if sizev>sizew:
        temp = Roots[w][0]
        for i,root in enumerate(Roots):
            if root[0]==temp:
                Roots[i][0]=Roots[v][0]
                Roots[i][1]=totalSize
            if root[0]==Roots[v][0]:
                    Roots[i][1]=totalSize
    else:
        temp = Roots[v][0]
        for i,root in enumerate(Roots):
            if root[0]==temp:
                Roots[i][0]=Roots[w][0]
                Roots[i][1]=totalSize
            if root[0]==Roots[w][0]:
                Roots[i][1]=totalSize

                
def connected(v,w):
    return findRoot(v)==findRoot(w)
