Roots=[]
Roots.append(0)#index of list => vertex; element of list => root

def initialize(n):
    global Roots
    Roots*=(n+1)
    for i in range(n+1):
        Roots[i]=i

def findRoot(v):
    while v!=Roots[v]:
        v=Roots[v]
    return v        

def union(v,w):
    rv = findRoot(v)
    rw = findRoot(w)
    Roots[rw] = rv

def connected(v,w):
    return findRoot(v)==findRoot(w)
