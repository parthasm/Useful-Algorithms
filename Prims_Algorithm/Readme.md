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

It stores the graph as a dictionary of dictionaries. Each vertex v is a key of the outer dictionary and it has a dictionary as a value. This inner dictionary lists all the vertices connected to the vertex v as keys and the edge weights as their corresponding values.

The time taken by the algorithm to run is reported.
