Prim's Algorithm
========

A python implementation of the Prim's algorithm to find the sum of the edge-weights of the 
Minimum Spanning Tree of a Graph.

http://en.wikipedia.org/wiki/Minimum_spanning_tree

http://en.wikipedia.org/wiki/Prim%27s_algorithm

##edges.txt

It is the input file listing all the edges. 
For each edge, there is a line in the text file listing the 2 connected vertices and the edge weight.
The only exception is the 1st line which lists the number of vertices and number of edges respectively.

##Prim_Double_Dictionary.py

It stores the graph as a dictionary of dictionaries. Each vertex v is a key of the outer dictionary and it has a dictionary as its value. This inner dictionary has the vertex w connected to vertex v as the key and the edge-weight e between the vertices w and v as the value.


##Prim_Dictionary_List.py

It stores the graph as a dictionary of lists. Each vertex v is a key of the outer dictionary and it has a list as its value. This list contains tuples. The 1st element of the tuple is the vertex w connected to vertex v and the 2nd element is the edge-weight e between the vertices w and v.


##Heap.py

It implements a heap as a list. Each element of this list is itself a list of length 2. The 1st inner element is the unprocessed vertex v and the 2nd inner element is the cost of the minimum-cost-edge connected to the vertex v which crosses from the set of unprocessed vertices to the set of processed vertices. 

##Prim_DD_Heap_Vertex.py

It stores the graph as a double dictionary as in 'Prim_Double_Dictionary.py',but uses a heap to store the least-cost edge crossing the set of processed vertices to the set of unprocessed vertices. 


The times taken by the algorithm to run for all the versions are reported. 'Prim_DD_Heap_Vertex.py' takes around half the time of the two other versions, due to a lower worst-time complexity.

The complexity of Prim's algorithm  in 'Prim_Double_Dictionary.py' and 'Prim_Dictionary_List.py' = O(mn)

The complexity of Prim's algorithm  in 'Prim_DD_Heap_Vertex.py' = O(m*log(n))

where,

m = #edges

n = #vertices
