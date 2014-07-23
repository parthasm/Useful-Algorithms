Roots=[]
Roots.append(0)#index of list => vertex; element of list => root

Sizes = []
Sizes.append(0)
def initialize(n):
    global Roots
    global Sizes
    Roots*=(n+1)
    Sizes*=(n+1)
    for i in range(1,n+1):
        Roots[i]=i
        Sizes[i]=1

def findRoot(v):
    while v!=Roots[v]:
        Roots[v] = Roots[Roots[v]]
        v=Roots[v]
    return v        

def union(v,w):
    rv = findRoot(v)
    rw = findRoot(w)
    if Sizes[rv] < Sizes[rw]:
        Roots[rv] = rw
        Sizes[rw]+=Sizes[rv]
    else:
        Roots[rw] = rv
        Sizes[rv]+=Sizes[rw]


def connected(v,w):
    return findRoot(v)==findRoot(w)
