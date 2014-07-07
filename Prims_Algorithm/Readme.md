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


The times taken by the algorithm to run for all the versions are reported. 

The complexity of Prim's algorithm  in 'Prim_Double_Dictionary.py' and 'Prim_Dictionary_List.py' is O(mn)

where m = #edges

      n = #vertices
