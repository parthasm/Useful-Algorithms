heap=[]
DictVertexToIndex={}
heap.append([0,0])
def sink(Index):
    NumVertices = len(heap)-1
    while 2*Index <= NumVertices:
        j = 2*Index
        if j < NumVertices and isGreaterThan(j,j+1):
            j=j+1
        if not isGreaterThan(Index,j):
            break
        exchange(Index,j)
        Index=j
        

def swim(Index):
    while Index > 1 and isGreaterThan(Index/2,Index):
        exchange(Index/2,Index)
        Index = Index/2

def isGreaterThan(Index1, Index2):
    return heap[Index1][1] > heap[Index2][1]

def isEmpty():
    return len(heap)<2

def exchange(Index1, Index2):
    heap[Index1] , heap[Index2] = heap[Index2] , heap[Index1]
    DictVertexToIndex[heap[Index1][0]]=Index1
    DictVertexToIndex[heap[Index2][0]]=Index2

def insert(vert):
    heap.append(vert)
    DictVertexToIndex[vert[0]]=len(heap)-1
    swim(len(heap)-1)

def printHeap():
    for vert in heap:
        print vert
        

def popMin():
    liMin = heap[1]
    exchange(1,len(heap)-1)
    heap.pop()
    sink(1)
    del DictVertexToIndex[liMin[0]]
    return liMin
    
def searchHeap(vertex):
    return DictVertexToIndex[vertex]
    
def lengthHeap():
    return (len(heap)-1)

def delVertexPopKey(vertex):
    ind = searchHeap(vertex)
    cost = heap[ind][1]
    exchange(ind,len(heap)-1)
    heap.pop()
    del DictVertexToIndex[vertex]
    sink(ind)
    return cost

def modifyKeyIfBetter(vertex,newEdgeCost):
    ind = searchHeap(vertex)
    cost = heap[ind][1]
    
    if newEdgeCost < cost:
        heap[ind][1]=newEdgeCost
        swim(ind)       
