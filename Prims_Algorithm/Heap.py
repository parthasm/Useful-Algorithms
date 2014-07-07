heap=[]
heap.append([0,0])
def sink(vertexIndex):
    NumVertices = len(heap)-1
    while 2*vertexIndex <= NumVertices:
        j = 2*vertexIndex
        if j < NumVertices and isGreaterThan(j,j+1):
            j=j+1
        if not isGreaterThan(vertexIndex,j):
            break
        exchange(vertexIndex,j)
        vertexIndex=j
        

def swim(vertexIndex):
    while vertexIndex > 1 and isGreaterThan(vertexIndex/2,vertexIndex):
        exchange(vertexIndex/2,vertexIndex)
        vertexIndex = vertexIndex/2

def isGreaterThan(vertexIndex1, vertexIndex2):
    return heap[vertexIndex1][1] > heap[vertexIndex2][1]

def isEmpty():
    return len(heap)<2

def exchange(vertexIndex1, vertexIndex2):
    heap[vertexIndex1] , heap[vertexIndex2] = heap[vertexIndex2] , heap[vertexIndex1]

def insert(vert):
    heap.append(vert)
    swim(len(heap)-1)

def printHeap():
    for vert in heap:
        print vert
        

def popMin():
    vert = heap[1]
    exchange(1,len(heap)-1)
    heap.pop()
    sink(1)
    return vert
    
def searchHeap(vertex):
    for index,li in enumerate(heap):
        if li[0]==vertex:
            return index

def lengthHeap():
    return (len(heap)-1)

def delVertexPopKey(vertex):
    ind = searchHeap(vertex)
    cost = heap[ind][1]
    exchange(ind,len(heap)-1)
    heap.pop()
    sink(ind)
    return cost

def modifyKeyIfBetter(vertex,newEdgeCost):
    ind = searchHeap(vertex)
    cost = heap[ind][1]
    
    if newEdgeCost < cost:
        heap[ind][1]=newEdgeCost
        swim(ind)       
