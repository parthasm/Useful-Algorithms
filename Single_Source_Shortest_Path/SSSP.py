Graph = {}

def setGraph(graph):
    global Graph
    Graph = graph

def BellmanFord(SourceVertex, OptimalFlag,NumVertices):
    A=[1000000]
    B=[1000000]
    A*=(NumVertices+1)
    B*=(NumVertices+1)
    A[SourceVertex]=0
    B[SourceVertex]=0
    for i in range(1,NumVertices+2):
        OptimaReached=True
        for v in Graph:
            minimum = A[v]
            ws = Graph[v]
            for w in ws:
                if minimum > ws[w]+A[w]:
                    minimum = ws[w]+A[w]
            B[v]=minimum
            if A[v]!=B[v]:
                OptimaReached=False
        if OptimalFlag and OptimaReached:
            break
        A=B[:]
    if not OptimaReached:
        print 'Graph has negative cycle'
        return []
    return A        


def DjikstraHeap(SourceVertex):
    import sys
    import os
    os.chdir("..")
    sys.path.append(os.getcwd())

    import Heap
    for v in Graph:
        if v!=SourceVertex:
            Heap.insert([v,1000000])
        else:
            Heap.insert([v,0])

    dict_shortest_path={}

    while Heap.lengthHeap() > 0 :
        w_score = Heap.popMin()
        w = w_score[0]
        dict_shortest_path[w]=w_score[1]
        di = Graph[w]
        for v in di:
            if dict_shortest_path.get(v,-1)==-1:
                Heap.modifyKeyIfBetter(v,w_score[1]+di[v])

    return dict_shortest_path
