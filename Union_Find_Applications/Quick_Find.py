Roots=[]
Roots.append(0)#index of list => vertex; element of list => root

def initialize(n):
    global Roots
    Roots*=(n+1)
    for i in range(n+1):
        Roots[i]=i

def findRoot(v):
    return Roots[v]       

def union(v,w):
    temp = Roots[w]
    for i,root in enumerate(Roots):
        if root==temp:
            Roots[i]=Roots[v]

def connected(v,w):
    return findRoot(v)==findRoot(w)
